
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.renderers import JSONRenderer
from users.backends import CookieJWTAuthentication
from datetime import *
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.conf import settings
from django.contrib.auth import get_user_model
import datetime
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django.middleware.csrf import get_token
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView

class CustomTokenRefreshView(TokenRefreshView):
    """
    Checks the validity of jwt access and refresh tokens stores as HTTP only cookies.

    Args:
        request: The HTTP request object.

    Returns:
        Response object with JSON data indicating if an access token or a refresh token was renewed or if the session expired.
    """
    def post(self, request, *args, **kwargs):

       
    
        refresh_token = request.COOKIES.get('refreshToken')
        last_interaction = request.data.get('last_interaction')  
        if not refresh_token:
            return Response({'error': 'Session expired. Please log in again.'}, status=401)

        try:
            old_refresh = RefreshToken(refresh_token)

            # Extract user ID and retrieve user
            user_id = old_refresh['user_id'] 
            user = get_user_model().objects.get(id=user_id)
           

            last_interaction_datetime = datetime.datetime.fromisoformat(last_interaction.replace('Z', '+00:00'))
            current_time = datetime.datetime.now(datetime.timezone.utc)
            time_difference = (current_time - last_interaction_datetime).total_seconds()

            refresh_expiration_timestamp = old_refresh['exp']
            refresh_expiration_datetime = datetime.datetime.fromtimestamp(refresh_expiration_timestamp, tz=datetime.timezone.utc)
            refresh_expires_in = (refresh_expiration_datetime - current_time).total_seconds()



            # If user was  active for the last 2 minutes and the refresh token expires in the next 5 minutes generate a new refresh token
            if time_difference < 120 and refresh_expires_in < 300:  
                old_refresh.blacklist()
                # Create a new refresh token for the user

                new_refresh = RefreshToken.for_user(user)
                new_refresh_token = str(new_refresh)
                new_access_token = str(new_refresh.access_token)

                response =  Response({'message': 'RefreshToken refreshed'}, status=200)

                if settings.HTTP_MODE:
                    response.set_cookie('refreshToken', new_refresh_token,
                    httponly=True, samesite=None, secure=False)
                    response.set_cookie('accessToken', new_access_token, httponly=True, samesite=None, secure=False)

                else:

                    response.set_cookie('refreshToken', new_refresh_token, domain=settings.DOMAIN_URL,
                    path="/", httponly=True, samesite=None, secure=True)
                    response.set_cookie('accessToken', new_access_token, domain=settings.DOMAIN_URL,
                    path="/", httponly=True, samesite=None, secure=True)

                return response
            # If user was  NOT active for the last 2 minutes and the refresh token expires in the next 5 minutes log the user out.
            elif time_difference >=120  and refresh_expires_in< 300:
                return Response({'error': 'Session expired. Please log in again.'}, status=401)

            # If the refresh token is not about to expire generate a new access token.
            else:

                access_token = str(old_refresh.access_token)
                response =  Response({'message': 'AccessToken refreshed'}, status=200)
                if settings.HTTP_MODE:
                    response.set_cookie('accessToken', access_token, httponly=True, samesite=None, secure=False)
                else:
                    response.set_cookie('accessToken', access_token, domain=settings.DOMAIN_URL,
                    path="/", httponly=True, samesite=None, secure=True)

                return response
        except Exception as e:
            return Response({'error': 'Session expired. Please log in again.'}, status=401)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_profile(request):
    """Tries to get an existing campagne object.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        Response: A Django REST Response object including the user profile. 
        Returns a success object when the user profile can be returned. Returns an error when the user profile cannot be found.
        200: If succesful
        404: If campagne object was not found

    Raises:
        Campagne.DoesNotExist: If campagne object was not found
    """
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=200)
    except UserProfile.DoesNotExist:
        return Response({'error': 'UserProfile not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_password_change_required(request):
    user = request.user
    try:
        user_profile = UserProfile.objects.get(user=user)
        return JsonResponse({'must_change_password': user_profile.must_change_password})
    except UserProfile.DoesNotExist:
        return Response({'error': 'UserProfile not found'}, status=status.HTTP_404_NOT_FOUND)

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

@permission_classes([AllowAny])
def ping_view(request):
    """
    Simple view to trigger middleware and set CSRF token.
    """
    return JsonResponse({'message': 'pong'})

@permission_classes([AllowAny])
@api_view(['POST'])
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
    elif user is None:
        return JsonResponse({'error': 'Invalid credentials.'}, status=401)

    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    response_data = {
        "message": "Authenticated successfully",
        "user": user.username,
    }
    csrf_token = get_token(request)
    

    response = Response(response_data)
    if settings.HTTP_MODE:
       
        response.set_cookie('accessToken', access_token,
             httponly=True, samesite=None, secure=False)
        response.set_cookie('refreshToken', refresh_token,
            httponly=True, samesite=None, secure=False)

    else:
        response.set_cookie(
            'csrfauthtoken',
            csrf_token,
            domain=settings.DOMAIN_URL,
            path="/",
            httponly=False,  
            samesite=None,  
            secure=True,     
        )
        response.set_cookie('accessToken', access_token, domain=settings.DOMAIN_URL,
            path="/", httponly=True, samesite=None, secure=True)
        response.set_cookie('refreshToken', refresh_token, domain=settings.DOMAIN_URL,
            path="/", httponly=True, samesite=None, secure=True)


    return response

@api_view(['GET'])
def logout_view(request):
    """
    Logs the user out and removes the cookies.

    Args:
        request: The HTTP request object containing username and password in the request data.

    Returns:
        Response object with JSON data containing the response with the removed cookies.
    """
    response = Response({"message": "Logged out successfully"})

    refresh_token = request.COOKIES.get('refreshToken')

    if not refresh_token and settings.HTTP_MODE:
        response.delete_cookie('accessToken',
        path="/")
        response.delete_cookie('refreshToken', 
        path="/")
        response.delete_cookie('csrfauthtoken',
        path="/")
        return response
    elif not refresh_token and not settings.HTTP_MODE:
        response.delete_cookie('accessToken', domain=settings.DOMAIN_URL,
        path="/")
        response.delete_cookie('refreshToken', domain=settings.DOMAIN_URL,
        path="/")
        response.delete_cookie('csrfauthtoken', domain=settings.DOMAIN_URL,
        path="/")
        return response

    try:
        # Attempt to blacklist the refresh token
        old_refresh = RefreshToken(refresh_token)
        old_refresh.blacklist()
    except (TokenError, InvalidToken) as e:
        # Handle specific JWT errors
        if settings.HTTP_MODE:
            response.delete_cookie('accessToken',
            path="/")
            response.delete_cookie('refreshToken', 
            path="/")
            response.delete_cookie('csrfauthtoken',
            path="/")

        else:
            response.delete_cookie('accessToken', domain=settings.DOMAIN_URL,
            path="/")
            response.delete_cookie('refreshToken', domain=settings.DOMAIN_URL,
            path="/")
            response.delete_cookie('csrfauthtoken', domain=settings.DOMAIN_URL,
            path="/")
        return response

    if settings.HTTP_MODE:
        response.delete_cookie('accessToken',
        path="/")
        response.delete_cookie('refreshToken', 
        path="/")
        response.delete_cookie('csrfauthtoken',
        path="/")
    else:
        # Invalidate the JWT cookies
        response.delete_cookie('accessToken', domain=settings.DOMAIN_URL,
            path="/")
        response.delete_cookie('refreshToken', domain=settings.DOMAIN_URL,
            path="/")
        response.delete_cookie('csrfauthtoken', domain=settings.DOMAIN_URL,
            path="/")

    return response



@permission_classes([IsAuthenticated])
class CustomPasswordChangeView(PasswordChangeView):
    """
    A custom class to change passwords. 

    Args:
        PasswordChangeView: The default django PasswordChangeView.
    """
    template_name = 'passwords/password_change_form.html'

    def dispatch(self, request, *args, **kwargs):
        """
        Called initially to check if the user is logged in. Otherwise password change cannot be processed.

        Args:
            request: The HTTP request object.

        Returns:
            A redirect to the frontend when password change was succesful to the dahboard otherwise to the login page.
        """
        jwt_auth = CookieJWTAuthentication()
        try:
            user, token = jwt_auth.authenticate(request)
            if user is not None:
                request.user = user
            else:
                return redirect((f'{settings.DOMAIN_URL}/login'))
        except InvalidToken:
            return redirect((f'{settings.DOMAIN_URL}/login'))

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return (f'{settings.DOMAIN_URL}/dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['domain_url'] = settings.DOMAIN_URL
        return context

    def form_valid(self, form):
        self.request.user.profile.must_change_password = False
        self.request.user.profile.save()
        return super().form_valid(form)

