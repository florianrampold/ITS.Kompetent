from importlib.resources import path
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'competence_tests', CompetenceTestViewSet)
router.register(r'competence_dimensions', CompetenceDimensionViewSet)
router.register(r'test_items', TestItemViewSet)
router.register(r'question_items', QuestionItemViewSet)
router.register(r'choice_items', ChoiceItemViewSet)
router.register(r'impulse_items', ImpulseItemViewSet)
router.register(r'image_items', ImageItemViewSet)
router.register(r'email_items', EmailItemViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('contact_request/', contact_request, name='contact_request'),
    path('generate_individual_report/', generate_individual_report, name='generate_individual_report'),



]



