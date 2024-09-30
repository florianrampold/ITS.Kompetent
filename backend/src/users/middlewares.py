

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from django.middleware.csrf import get_token
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings



class JWTWithCSRFMiddleware(MiddlewareMixin):
    
     # Define the paths or views that should be CSRF-protected
    protected_routes = {
        '/api/create_campagne/',
        '/api/post_invitations/',
        '/api/delete_campagne/',
        '/api/decrypt_emails/',
        '/api/remove_security_key/',
        '/api/invalidate_invitation_tokens/',
        '/api/end_campaign/',

    }
    def process_response(self, request, response):
       
        if not request.path.startswith('/admin/'):
            # Set a cookie on the response object
            if not request.COOKIES.get('csrfauthtoken'):
                response.set_cookie(
                'csrfauthtoken',
                get_token(request),  # Generate a new CSRF token,
                httponly=False,  # Allow access via JavaScript
                samesite=None,  
                secure=False,     # Use `False` in development if not on HTTPS
            )
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

       

        # Check if the request is POST and the path is in protected_routes
        if request.path in self.protected_routes:
            csrf_token_header = request.headers.get('X-CSRFToken')
            csrf_token_cookie = request.COOKIES.get('csrfauthtoken')

            if not csrf_token_header or not csrf_token_cookie or csrf_token_header != csrf_token_cookie:
                return HttpResponseForbidden('CSRF cookie not set')

        return None


class EnforcePasswordChangeMiddleware:
    """
    Middleware to enforce password change for users who must change their password.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
    # If the user is authenticated and must change their password
        if request.COOKIES.get('accessToken') and not request.path.startswith('/admin/'):
            refresh_token = request.COOKIES.get('refreshToken')
            
            if refresh_token:
                old_refresh = RefreshToken(refresh_token)

                try:
                    user_id = old_refresh['user_id'] 
                    user = get_user_model().objects.get(id=user_id)

                    if user.profile.must_change_password:
                        if request.path.startswith('/api/get_campagne/'):
                            return JsonResponse({
                                'error': 'password_change_required',
                                'message': 'You must change your password before accessing this resource.'
                            }, status=403)
                
                except get_user_model().DoesNotExist:
                    response = JsonResponse({
                    'error': 'user_not_found',
                    'message': 'User does not exist or session is invalid. Logging out.'
                     }, status=403)
                    response.delete_cookie('accessToken', domain=settings.DOMAIN_URL,
                    path="/")
                    response.delete_cookie('refreshToken', domain=settings.DOMAIN_URL,
                    path="/")
                    response.delete_cookie('csrfauthtoken', domain=settings.DOMAIN_URL,
                    path="/")

        return self.get_response(request)