
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'trainings', TrainingViewSet)
router.register(r'training_categories', TrainingCategoryViewSet)





urlpatterns = router.urls