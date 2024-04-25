
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import JSONRenderer
from users.backends import CookieJWTAuthentication
from datetime import *
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenRefreshView
import datetime
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

class CustomTokenRefreshView(TokenRefreshView):
    """
    Chekcs the validity of jwt access and refresh tokens stores as HTTP only cookies.

    Args:
        request: The HTTP request object.

    Returns:
        Response object with JSON data indicating if an access token or a refresh token was renewed or if the session expired.
    """
    def post(self, request, *args, **kwargs):
    
        refresh_token = request.COOKIES.get('refreshToken')
        last_interaction = request.data.get('last_interaction')  # Receive the activity status from the request
        if not refresh_token:
            return Response({'error': 'Session expired. Please log in again.'}, status=401)

        try:
            old_refresh = RefreshToken(refresh_token)
            # Extract user ID and retrieve user
            user_id = old_refresh['user_id']  # Ensure 'user_id' is part of the token payload when issued
            user = get_user_model().objects.get(id=user_id)
            last_interaction_datetime = datetime.datetime.fromisoformat(last_interaction.replace('Z', '+00:00'))
            current_time = datetime.datetime.now(datetime.timezone.utc)
            time_difference = (current_time - last_interaction_datetime).total_seconds()

            expiration_timestamp = old_refresh['exp']
            expiration_datetime = datetime.datetime.fromtimestamp(expiration_timestamp, tz=datetime.timezone.utc)
            expires_in = (expiration_datetime - current_time).total_seconds()


            # If user was  active for the last 2 minutes and the refresh token expires in the next 5 minutes generate a new refresh token
            if time_difference < 120 and expires_in < 300:  
                print("RENEW REFRESH")
                old_refresh.blacklist()
                # Create a new refresh token for the user
                new_refresh_lifetime = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']

                new_refresh = RefreshToken.for_user(user)
                new_refresh_token = str(new_refresh)
                new_access_token = str(new_refresh.access_token)

                response =  Response({'message': 'RefreshToken refreshed'}, status=200)

                response.set_cookie('refreshToken', new_refresh_token, httponly=True, samesite='Lax', secure=True, max_age=int(new_refresh_lifetime.total_seconds()))
                response.set_cookie('accessToken', new_access_token, httponly=True, samesite='Lax', secure=False, max_age=int(new_refresh.access_token.lifetime.total_seconds()))
                return response
            # If user was  NOT active for the last 2 minutes and the refresh token expires in the next 5 minutes log the user out.
            elif time_difference >=120  and expires_in < 300:
                print("INVALIDATE REFRESH")
                return Response({'error': 'Session expired. Please log in again.'}, status=401)

            # If the refresh token is not about to expire generate a new access token.
            else:
                print("GENERATE NEW ACCESS TOKEN WITH OLD REFRESH")
                access_token = str(old_refresh.access_token)
                response =  Response({'message': 'AccessToken refreshed'}, status=200)
                response.set_cookie('accessToken', access_token, httponly=True, samesite='Lax', secure=False, max_age=int(old_refresh.access_token.lifetime.total_seconds()))

                return response
        except Exception as e:
            print("exception")
            return Response({'error': str(e)}, status=401)


@api_view(['GET'])
@authentication_classes([CookieJWTAuthentication])
@permission_classes([IsAuthenticated])
def status(request):
    """
    View to retrieve user authentication status.

    Args:
        request: The HTTP request object.

    Returns:
        Response object with JSON data indicating the authentication status and the username of the authenticated user.
    """
    response = Response({"status": "authenticated", "user": str(request.user.username)})
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def obtain_jwt_token_with_cookie(request):
    """
    View to obtain JWT token with cookie authentication.

    Args:
        request: The HTTP request object containing username and password in the request data.

    Returns:
        Response object with JSON data containing the authentication token, expiration details, and user information.
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)
    if user is not None and user.is_active:
        if not user.profile.is_campagne_manager:
            return JsonResponse({'error': 'Only Campagne Managers can log in.'}, status=403)
        # Proceed with login logic for non-admin users
        # ...
    elif user is None:
        return JsonResponse({'error': 'Invalid credentials.'}, status=401)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)
    refresh_lifetime = settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME']



    response_data = {
        "message": "Authenticated successfully",
        "user": user.username,
    }

    response = Response(response_data)
    response.set_cookie('accessToken', access_token, httponly=True, samesite='Lax', secure=True, max_age=int(refresh.access_token.lifetime.total_seconds()))
    response.set_cookie('refreshToken', refresh_token, httponly=True, samesite='Lax', secure=True, max_age=refresh_lifetime.total_seconds())


    return response

@api_view(['POST'])
@permission_classes([AllowAny])
def logout_view(request):
    """
    View to log out the user and invalidate the JWT cookie.

    Args:
        request: The HTTP request object.

    Returns:
        Response object with a message indicating successful logout.
    """
    response = Response({"message": "Logged out successfully"})
    refresh_token = request.COOKIES.get('refreshToken')
    old_refresh = RefreshToken(refresh_token)
    old_refresh.blacklist()



    # Invalidate the JWT cookie
    response.delete_cookie('accessToken')
    response.delete_cookie('refreshToken')


    return response


