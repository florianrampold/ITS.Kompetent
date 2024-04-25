from rest_framework.serializers import ModelSerializer
from .models import *
from threats.serializers import ThreatVectorSerializer, ThreatSituationSerializer
from rest_polymorphic.serializers import PolymorphicSerializer

class CompetenceTestSerializer(ModelSerializer):
    """
    Serializer for CompetenceTest model.

    Serializes CompetenceTest objects with their associated threat vectors.

    Attributes:
        threat_situations: A list of ThreatSituationSerializer instances associated with the competence test.
    """

    #threat_vector = ThreatVectorSerializer(many=True, read_only=True)
    #threat_situations = ThreatSituationSerializer(many=True, read_only=True)


    class Meta:
        model = CompetenceTest
        fields = ['id', 'threat_situations']
        depth=3


class CompetenceDimensionSerializer(ModelSerializer):
    """
    Serializer for CompetenceDimension model.

    Serializes CompetenceDimension objects.

    Attributes:
        id: The unique identifier of the competence dimension.
        dimension_name: The name of the competence dimension.
        dimension_description: The description of the competence dimension.
    """

    class Meta:
        model = CompetenceDimension
        fields = ['id', 'dimension_name', 'dimension_description']

class QuestionItemSerializer(ModelSerializer):
    """
    Serializer for QuestionItem model.

    Serializes QuestionItem objects.

    Attributes:
        id: The unique identifier of the question item.
        question_name: The name of the question item.
        question: The question text.
        type: The type of the question item.
    """

    class Meta:
        model = QuestionItem
        fields = ['id', 'question_name', 'question', 'type']

class ImpulseItemSerializer(ModelSerializer):
    """
    Serializer for ImpulseItem model.

    Serializes ImpulseItem objects.

    Attributes:
        id: The unique identifier of the impulse item.
        impulse_name: The name of the impulse item.
    """

    class Meta:
        model = Impulse
        fields =['id', 'impulse_name']

class TestItemSerializer(ModelSerializer):
    """
    Serializer for CompetenceTestItem model.

    Serializes CompetenceTestItem objects.

    Attributes:
        question_item: A list of QuestionItemSerializer instances associated with the competence test item.
        impulse_item: The ImpulseItemSerializer instance associated with the competence test item.
        competence_dimension: The CompetenceDimensionSerializer instance associated with the competence test item.
    """

    question_item = QuestionItemSerializer(many=True, read_only=True)
    impulse_item = ImpulseItemSerializer(read_only=True)
    competence_dimension= CompetenceDimensionSerializer(read_only=True)

    class Meta:
        model = CompetenceTestItem
        fields = ["question_item", "impulse_item", "competence_dimension"]
 
class EmailImpulseSerializer(ModelSerializer):
    """
    Serializer for EmailImpulse model.

    Serializes EmailImpulse objects.

    Attributes:
        id: The unique identifier of the email impulse.
        email: The email associated with the impulse.
        impulse_text: The text content of the impulse.
    """

    class Meta:
        model = EmailImpulse
        fields =['id', 'email', 'impulse_text']
        depth=1

class ImageImpulseSerializer(ModelSerializer):
    """
    Serializer for ImageImpulse model.

    Serializes ImageImpulse objects.

    Attributes:
        id: The unique identifier of the image impulse.
        image: The image associated with the impulse.
        impulse_text: The text content of the impulse.
    """

    class Meta:
        model = ImageImpulse
        fields =['id', 'image', 'impulse_text']
        depth=1

class ChatInterfaceSerializer(ModelSerializer):
    """
    Serializer for ChatInterface model.

    Serializes ChatInterface objects.

    Attributes:
        id: The unique identifier of the chat interface.
        chat_sender_name: The name of the chat sender.
        chat_sender_known: Boolean indicating whether the chat sender is known or not.
        chat_sender_image: The image of the chat sender.
        chat_message_incoming: The incoming chat message.
        chat_message_incoming_date: The date of the incoming chat message.
        chat_message_outgoing: The outgoing chat message.
        chat_message_outgoing_date: The date of the outgoing chat message.
        chat_message_incoming_2: The second incoming chat message.
        chat_message_incoming_date_2: The date of the second incoming chat message.
    """

    class Meta:
        model = ChatInterface
        fields = ['id', 'chat_sender_name', 'chat_sender_known', 'chat_sender_image',
                  'chat_message_incoming', 'chat_message_incoming_date',
                  'chat_message_outgoing', 'chat_message_outgoing_date',
                  'chat_message_incoming_2', 'chat_message_incoming_date_2']

class ChatImpulseSerializer(ModelSerializer):
    """
    Serializer for ChatImpulse model.

    Serializes ChatImpulse objects.

    Attributes:
        id: The unique identifier of the chat impulse.
        chat_interface: The associated chat interface.
        impulse_text: The text content of the impulse.
    """

    class Meta:
        model = ChatImpulse
        fields = ['id', 'chat_interface', 'impulse_text']
        depth=1

class ImageItemSerializer(ModelSerializer):
    """
    Serializer for ImageItem model.

    Serializes ImageItem objects.

    Attributes:
        id: The unique identifier of the image item.
        image_name: The name of the image.
        image_field: The image file.
    """

    class Meta:
        model = ImageItem
        fields = ['id', 'image_name', 'image_field']


class EmailItemSerializer(ModelSerializer):
    """
    Serializer for EmailItem model.

    Serializes EmailItem objects.

    Attributes:
        id: The unique identifier of the email item.
        email_name: The name of the email.
        email_sender: The sender of the email.
        email_recipient: The recipient of the email.
        email_regarding: The subject of the email.
        email_content: The content of the email.
        email_image_sender: The image of the email sender.
    """

    class Meta:
        model = EmailItem
        fields = ['id', 'email_name', 'email_sender', 'email_recipient', 'email_regarding', 'email_content', 'email_image_sender']

class ChoiceItemSerializer(ModelSerializer):
    """
    Serializer for ChoiceItem model.

    Serializes ChoiceItem objects.

    Attributes:
        id: The unique identifier of the choice item.
        option: The option of the choice item.
        answer_rating: The rating of the answer.
    """

    class Meta:
        model = ChoiceItem
        fields = ['id', 'option', 'answer_rating']

class ImpulseItemPolymorphicSerializer(PolymorphicSerializer):
    """
    Polymorphic serializer for ImpulseItem model.

    Serializes different types of impulse items.

    Attributes:
        model_serializer_mapping: Mapping of impulse item models to their respective serializers.
    """

    model_serializer_mapping = {
        Impulse: ImpulseItemSerializer,
        EmailImpulse: EmailImpulseSerializer,
        ImageImpulse: ImageImpulseSerializer,
        ChatImpulse: ChatImpulseSerializer,
    }