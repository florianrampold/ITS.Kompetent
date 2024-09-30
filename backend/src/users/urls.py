# urls.py

from django.urls import path, include
from .views import check_password_change_required
from .views import  CustomTokenRefreshView, obtain_jwt_token_with_cookie, logout_view, status, get_user_profile, ping_view
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/jwt/', include('djoser.urls.jwt')),
    path('auth/jwt/create/', obtain_jwt_token_with_cookie, name='obtain_jwt_token_with_cookie'),
    path('auth/jwt/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('status/', status, name='status'),
    path('logout/', logout_view, name='logout'),
    path('check_password_change/', check_password_change_required, name='check_password_change'),
    path('ping/', ping_view, name='ping'),

    



]
