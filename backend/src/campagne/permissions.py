from rest_framework.permissions import BasePermission
from django.conf import settings
class IsFromFrontendApp(BasePermission):
    """
    Custom permission to only allow requests from the frontend application.
    """

    def has_permission(self, request, view):
        allowed_origins = [settings.DOMAIN_URL]
        return request.META.get('HTTP_ORIGIN') in allowed_origins
