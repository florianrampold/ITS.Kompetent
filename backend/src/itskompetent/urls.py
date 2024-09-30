"""itskompetent URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from django.conf import settings
from django.contrib.auth import views as auth_views
from users.views import CustomPasswordChangeView


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='passwords/login.html',
    ), name='login'),
    path('admin/', admin.site.urls),
    path('api/', include('job_profiles.urls')),
    path('api/', include('threats.urls')),
    path('api/', include('competence_tests.urls')),
    path('api/', include('campagne.urls')), 
    path('api/', include('trainings.urls')),
    path('api/', include('users.urls')),
    path('accounts/password_change/', CustomPasswordChangeView.as_view(
       template_name='passwords/password_change_form.html',
    ), name='password_change'),
    path('accounts/', include('django.contrib.auth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'ITS.kompetent Admin'