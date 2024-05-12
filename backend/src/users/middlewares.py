class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware, REASON_NO_CSRF_COOKIE
from rest_framework.authentication import get_authorization_header
from django.http import HttpResponseForbidden
from django.middleware.csrf import get_token
from rest_framework.response import Response

class JWTWithCSRFMiddleware(MiddlewareMixin):
    
     # Define the paths or views that should be CSRF-protected
    protected_routes = {
        '/api/create_campagne/',
        '/api/post_invitations/',
        '/api/delete_campagne/',
        '/api/decrypt_emails/',
        '/api/remove_security_key/',
    }
    def process_response(self, request, response):

        # Set a cookie on the response object
        if not request.COOKIES.get('csrfauthtoken'):
            response.set_cookie(
            'csrfauthtoken',
            get_token(request),  # Generate a new CSRF token,
            httponly=False,  # Allow access via JavaScript
            samesite=None,  # Adjust as needed for your application
            secure=False,     # Use `False` in development if not on HTTPS
        )
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

       

        # Check if the request is POST and the path is in protected_routes
        if request.path in self.protected_routes:
            csrf_token_header = request.headers.get('X-CSRFToken')
            csrf_token_cookie = request.COOKIES.get('csrfauthtoken')
            print(csrf_token_cookie, "cookie")

            if not csrf_token_header or not csrf_token_cookie or csrf_token_header != csrf_token_cookie:
                return HttpResponseForbidden('CSRF cookie not set')

        return None