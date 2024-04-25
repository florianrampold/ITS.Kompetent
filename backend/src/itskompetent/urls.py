"""itskompetent URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import views as auth_views

def redirect_to_frontend_login(request):
    if settings.DEBUG:
        login_url = 'http://localhost:8080/login'
    else: 
        login_url = 'https://itskompetent.uni-goettingen.de/login'
    next_url = request.GET.get('next', '')
    if next_url:
        login_url = f"{login_url}?next={next_url}"
    return HttpResponseRedirect(login_url)

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('accounts/login/', redirect_to_frontend_login, name='login'),
    path('admin/', admin.site.urls),
    path('api/', include('job_profiles.urls')),
    path('api/', include('threats.urls')),
    path('api/', include('competence_tests.urls')),
    path('api/', include('campagne.urls')), 
    path('api/', include('trainings.urls')),
    path('api/', include('users.urls')),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        email_template_name='passwords/custom_password_reset_email.txt',
        html_email_template_name='passwords/custom_password_reset_email.html',
    ), name='password_reset'),
    path('accounts/', include('django.contrib.auth.urls')),

    # urls.py

   # path('api/auth/', include('djoser.urls')),
    #path('api/auth/', include('djoser.urls.jwt')),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ITS.kompetent Admin'