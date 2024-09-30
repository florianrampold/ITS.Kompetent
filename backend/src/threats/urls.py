
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'threat_events', ThreatEventViewSet)
router.register(r'threat_areas', ThreatAreaViewSet)
router.register(r'threat_vectors', ThreatVectorViewSet)
router.register(r'threat_situations', ThreatSituationViewSet)



urlpatterns = router.urls