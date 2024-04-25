from rest_framework.serializers import ModelSerializer

from .models import ThreatArea
from .models import ThreatVector
from .models import ThreatEvent
from .models import ThreatSituation

class ThreatAreaSerializer(ModelSerializer):
    """
    Serializer for ThreatArea model.

    Serializes ThreatArea objects.

    Attributes:
        id: The unique identifier of the threat area.
        area_name: The name of the threat area.
        area_description: The description of the threat area.
    """

    class Meta:
        model = ThreatArea
        fields = ['id', 'area_name', 'area_description']


class ThreatEventSerializer(ModelSerializer):
    """
    Serializer for ThreatEvent model.

    Serializes ThreatEvent objects.

    Attributes:
        id: The unique identifier of the threat event.
        event_name: The name of the threat event.
        event_description: The description of the threat event.
    """

    class Meta:
        model = ThreatEvent
        fields = ['id', 'event_name', 'event_description']


class ThreatVectorSerializer(ModelSerializer):
    """
    Serializer for ThreatVector model.

    Serializes ThreatVector objects with their associated threat area and threat event.

    Attributes:
        threat_area: The ThreatAreaSerializer instance associated with the threat vector.
        threat_event: The ThreatEventSerializer instance associated with the threat vector.
        threat_vector_description: The description of the threat vector.
    """

    threat_area = ThreatAreaSerializer(read_only=True)
    threat_event = ThreatEventSerializer(read_only=True)

    class Meta:
        model = ThreatVector
        fields = ['id', 'threat_area', 'threat_event', "threat_vector_description"]


class ThreatSituationSerializer(ModelSerializer):
    """
    Serializer for ThreatSituation model.

    Serializes ThreatSituation objects.

    Attributes:
        id: The unique identifier of the threat situation.
        threat_description: The description of the threat situation.
        threat_vector: The associated threat vector.
        job_profile: The associated job profile.
    """

    class Meta:
        model = ThreatSituation
        fields = ['id', 'threat_description', 'threat_vector', 'job_profile']