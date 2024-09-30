
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import JobProfile
from threats.models import  ThreatSituation, ThreatEvent, ThreatVector
from trainings.models import TrainingCategory
from .serializers import JobProfileSerializer
from threats.serializers import ThreatEventSerializer, ThreatAreaSerializer

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


@api_view(['GET'])
def threat_events_by_job_profiles(request):
    """
    Gets all job profiles asscoiated with a training category.

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200, else returns an internal server error.
    """
    try:
        all_job_profiles = JobProfile.objects.filter(show_job_profile=True).distinct()
        result = []

        for job_profile in all_job_profiles:
            threat_situations = ThreatSituation.objects.filter(job_profile=job_profile)
            threat_vectors = threat_situations.values_list('threat_vector', flat=True)
            threat_events = ThreatEvent.objects.filter(threatvector__in=threat_vectors).distinct()

            distinct_threat_situations_count = ThreatSituation.objects.filter(
                    job_profile=job_profile,
                    threat_vector__threat_event__in=threat_events
                ).distinct().count()

            serialized_threat_events = ThreatEventSerializer(threat_events, many=True).data

            # Add threat categories to each serialized threat event
            for threat_event_data in serialized_threat_events:
                threat_event_id = threat_event_data['id']
                threat_event = ThreatEvent.objects.get(id=threat_event_id)
                threat_categories = TrainingCategory.objects.filter(threat_event__id=threat_event_id).distinct()
                threat_event_data['threat_categories'] = [
                    {
                        'category_name': category.training_category_name,
                        'category_description': category.training_category_description
                    } for category in threat_categories
                ]
                threat_vectors = ThreatVector.objects.filter(threat_event=threat_event, threatsituation__job_profile=job_profile).distinct()
                threat_areas = [tv.threat_area for tv in threat_vectors]
                threat_event_data['threat_areas'] = ThreatAreaSerializer(threat_areas, many=True).data
            result.append({
                'job_profile_id': job_profile.id,
                'job_profile_name': job_profile.job_name,
                'job_profile_description': job_profile.job_description,
                'distinct_threat_situations_count': distinct_threat_situations_count,
                'threat_events':  serialized_threat_events
            })

        return Response(result, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
