from rest_framework.serializers import ModelSerializer
from job_profiles.serializers import *
from .models import *
from rest_framework import serializers
from threats.serializers import ThreatEventSerializer

class TrainingGroupSerializer(ModelSerializer):
    """
    Serializer for TrainingGroup model.

    Serializes TrainingGroup objects.

    Attributes:
        id: The unique identifier of the training group.
        identifier: The identifier of the training group.
    """

    class Meta:
        model = TrainingGroup
        fields = ['id', 'identifier']

class LanguageSerializer(ModelSerializer):
    """
    Serializer for Language model.

    Serializes Language objects.

    Attributes:
        id: The unique identifier of the language.
        language: The language.
    """

    class Meta:
        model = Language
        fields = ['id', 'language']

class DeliveryMethodSerializer(ModelSerializer):
    """
    Serializer for DeliveryMethod model.

    Serializes DeliveryMethod objects.

    Attributes:
        id: The unique identifier of the delivery method.
        delivery_method: The delivery method.
    """

    class Meta:
        model = DeliveryMethod
        fields = ['id', 'delivery_method']

class TrainingSerializer(ModelSerializer):
    """
    Serializer for Training model.

    Serializes Training objects with additional fields.

    Attributes:
        training_group: The TrainingGroupSerializer instance associated with the training.
        competence_dimension_count: The count of competence dimensions associated with the training.
        costs_name: The display name of the training's costs.
        certification: The display name of the training's certification.
    """

    training_group = TrainingGroupSerializer(read_only=True)
    competence_dimension_count = serializers.SerializerMethodField()
    costs_name = serializers.CharField(source='get_costs_display')
    certification = serializers.CharField(source='get_certification_display')

    class Meta:
        model = Training
        fields = ['id', 'training_group', 'training_provider', 'training_name','delivery_method', 'costs_name', 'certification', 'language', 'training_url', 'competence_dimensions', 'threat_event', 'competence_dimension_count']
        depth=1

    def get_competence_dimension_count(self, training):
        """
        Gets the count og competence dimensions assigned to a training program

        Args:
            training (model): The model of the training

        Returns:
            - Returns the count.
        """
        return training.competence_dimensions.count()



class TrainingCategorySerializer(ModelSerializer):
    """
    Serializer for ThreatVector model.

    Serializes ThreatVector objects with their associated threat area and threat event.

    Attributes:
        training_category_name: The name of the training category.
        training_category_description: The description of the training categeory.
        threat_area: The ThreatAreaSerializer instance associated with the threat vector.
        threat_event: The ThreatEventSerializer instance associated with the threat vector.
        threat_vector_description: The description of the threat vector.
    """

    threat_event = ThreatEventSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingCategory
        fields = ["id", "training_category_name", "training_category_description", 'threat_event']




