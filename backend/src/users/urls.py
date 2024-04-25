# urls.py

from django.urls import path, include
from .views import  CustomTokenRefreshView, obtain_jwt_token_with_cookie, logout_view, status
urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/jwt/', include('djoser.urls.jwt')),
    path('auth/jwt/create/', obtain_jwt_token_with_cookie, name='obtain_jwt_token_with_cookie'),
    path('auth/jwt/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('status/', status, name='status'),
    path('logout/', logout_view, name='logout'),
    
    #path('accounts/', include('django.contrib.auth.urls')),



]
