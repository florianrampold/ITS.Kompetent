from importlib.resources import path
from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('job_profiles', JobProfilesViewSet)


urlpatterns = router.urls