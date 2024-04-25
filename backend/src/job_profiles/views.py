
# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import JobProfile
from .serializers import JobProfileSerializer

class JobProfilesViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on job profiles.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting job profiles.
    
    Attributes:
        queryset (QuerySet): The queryset containing all job profiles.
        serializer_class (Serializer): The serializer class used for job profile serialization and deserialization.
    """
    queryset = JobProfile.objects.all()
    serializer_class = JobProfileSerializer


