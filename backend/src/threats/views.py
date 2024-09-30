
from rest_framework.viewsets import ModelViewSet

from .models import ThreatArea
from .models import ThreatVector
from .models import ThreatEvent
from .models import ThreatSituation

from .serializers import ThreatAreaSerializer
from .serializers import ThreatEventSerializer
from .serializers import ThreatVectorSerializer
from .serializers import ThreatSituationSerializer


class ThreatAreaViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on threat areas.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting threat areas.
    
    Attributes:
        queryset (QuerySet): The queryset containing all threat areas.
        serializer_class (Serializer): The serializer class used for threat areas serialization and deserialization.
    """
    queryset = ThreatArea.objects.all()
    serializer_class = ThreatAreaSerializer


class ThreatEventViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on threat events.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting threat events.
    
    Attributes:
        queryset (QuerySet): The queryset containing all threat events.
        serializer_class (Serializer): The serializer class used for threat events serialization and deserialization.
    """
    queryset = ThreatEvent.objects.all()
    serializer_class = ThreatEventSerializer


class ThreatVectorViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on threat vectors.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting threat vectors.
    
    Attributes:
        queryset (QuerySet): The queryset containing all threat vectors.
        filter_fields (Filter): Allows to filter threat vectors by assigned job profile
        serializer_class (Serializer): The serializer class used for threat vectors serialization and deserialization.
    """
    queryset = ThreatVector.objects.all()
    serializer_class = ThreatVectorSerializer
    filterset_fields = ['job_profile']


class ThreatSituationViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on threat situations.

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting threat situations.
    
    Attributes:
        queryset (QuerySet): The queryset containing all threat situations.
        filter_fields (Filter): Allows to filter threat vectors by assigned job profile and threat vector
        serializer_class (Serializer): The serializer class used for threat situations serialization and deserialization.
    """
    queryset = ThreatSituation.objects.all()
    serializer_class = ThreatSituationSerializer
    filterset_fields = ['threat_vector', 'job_profile']

