from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import JobProfile

class JobProfileSerializer(ModelSerializer):
    """
    Serializer for JobProfile model.

    Serializes JobProfile objects.

    Attributes:
        id: The unique identifier of the job profile.
        job_name: The name of the job profile.
        job_description: The description of the job profile.
        job_tasks: The description of the job profile tasks.
        show_job_profile: Determines whether the job profile should be displayed in the frontend
        threat_count: The distinct number of threa vectors associated with the job profile.
    """
    threat_count = serializers.SerializerMethodField()
    class Meta:
        model = JobProfile
        fields = ['id', 'job_name', 'job_description', 'job_tasks', 'show_job_profile', 'threat_count']

    def get_threat_count(self, obj):
        """
        Count the threat_vectors related to a job profile.

        Returns:
            (int): The number of associated threat vectors
        """
        if obj.id in self.context.get('threat_counts', {}):
            return self.context['threat_counts'][obj.id]
        return 0