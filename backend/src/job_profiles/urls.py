from importlib.resources import path
from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('job_profiles', JobProfilesViewSet)

custom_urlpatterns = [
    path('job_profiles_by_training_categories', threat_events_by_job_profiles, name='job_profiles_by_threat_category'),
]

urlpatterns = router.urls + custom_urlpatterns