from importlib.resources import path
from django.urls import path
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'trainings', TrainingViewSet)
#router.register(r'trainings_content', TrainingsContentViewSet)




urlpatterns = router.urls