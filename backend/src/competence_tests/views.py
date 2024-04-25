from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet
from .models import CompetenceDimension
from .models import *
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from job_profiles.models import JobProfile
from competence_tests.models import CompetenceDimension
from weasyprint import HTML
import json
from .charts import  *

class CompetenceDimensionViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on competence dimensions

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting competence dimensions.
    
    Attributes:
        queryset (QuerySet): The queryset containing all competence dimensions.
        serializer_class (Serializer): The serializer class used for competence dimensions serialization and deserialization.
    """
    queryset = CompetenceDimension.objects.all()
    serializer_class = CompetenceDimensionSerializer

class CompetenceTestViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on competence tests

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting competence tests
    
    Attributes:
        queryset (QuerySet): The queryset containing all competence tests.
        serializer_class (Serializer): The serializer class used for competence tests serialization and deserialization.
    """
    queryset = CompetenceTest.objects.all()
    filterset_fields = ['job_profile']
    serializer_class = CompetenceTestSerializer

class QuestionItemViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on questions

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting questions.
    
    Attributes:
        queryset (QuerySet): The queryset containing all questions.
        serializer_class (Serializer): The serializer class used for questions serialization and deserialization.
    """
    queryset = QuestionItem.objects.all()
    serializer_class = QuestionItemSerializer

class TestItemViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on competence test scenarios

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting competence test scenarios.
    
    Attributes:
        queryset (QuerySet): The queryset containing all competence test scenarios.
        serializer_class (Serializer): The serializer class used for competence test scenarios serialization and deserialization.
    """
    queryset = CompetenceTestItem.objects.all()
    filterset_fields = ['threat_situation']
    serializer_class = TestItemSerializer



class ImpulseItemViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on impulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting impulses.
    
    Attributes:
        queryset (QuerySet): The queryset containing all impulses.
        filter_fields (Filter): Allows to filter impulses
        serializer_class (Serializer): The serializer class used for impulses serialization and deserialization.
    """
    queryset = Impulse.objects.all()
    filter_fields = {
            'id': ["in", "exact"],
    }    
    serializer_class =ImpulseItemPolymorphicSerializer


class ImageItemViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on images for ImageImpulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting images.
    
    Attributes:
        queryset (QuerySet): The queryset containing all images.
        serializer_class (Serializer): The serializer class used for images serialization and deserialization.
    """
    queryset = ImageItem.objects.all()
    serializer_class = ImageItemSerializer

class EmailItemViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on e-mails for E-MailImpulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting e-mails.
    
    Attributes:
        queryset (QuerySet): The queryset containing all e-mails.
        serializer_class (Serializer): The serializer class used for e-mail serialization and deserialization.
    """
    queryset = EmailItem.objects.all()
    serializer_class = EmailItemSerializer


class ChatInterfaceViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on chats for ChatImpulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting chats.
    
    Attributes:
        queryset (QuerySet): The queryset containing all chats.
        serializer_class (Serializer): The serializer class used for chat serialization and deserialization.
    """
    queryset = ChatInterface.objects.all()
    serializer_class = ChatInterfaceSerializer

class ImageImpulseViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on images impulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting image impulses.
    
    Attributes:
        queryset (QuerySet): The queryset containing all image impulses.
        serializer_class (Serializer): The serializer class used for image impulses serialization and deserialization.
    """
    queryset = ImageImpulse.objects.all()
    serializer_class = ImageImpulseSerializer

class EmailImpulseViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on e-mail impulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting e-mail impulses.
    
    Attributes:
        queryset (QuerySet): The queryset containing all e-mail impulses.
        serializer_class (Serializer): The serializer class used for e-mail impulses serialization and deserialization.
    """
    queryset = EmailImpulse.objects.all()
    serializer_class = EmailImpulseSerializer

class ChatImpulseViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on chat impulses

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting chat impulses.
    
    Attributes:
        queryset (QuerySet): The queryset containing all chat impulses.
        serializer_class (Serializer): The serializer class used for chat impulses serialization and deserialization.
    """
    queryset = ChatImpulse.objects.all()
    serializer_class = ChatImpulseSerializer
    
class ChoiceItemViewSet(ModelViewSet):
    """
    A ViewSet for handling CRUD operations on answer options for a dedictaed question

    This ViewSet provides endpoints for creating, retrieving, updating, and deleting answer options.
    
    Attributes:
        queryset (QuerySet): The queryset containing all answer options.
        filter_fields (Filter): Allows to filter for specific questions
        serializer_class (Serializer): The serializer class used for answer option serialization and deserialization.
    """
    queryset = ChoiceItem.objects.all()
    filterset_fields = ['question']
    serializer_class = ChoiceItemSerializer

        
def contact_request(request):
    """
    Tries to send a contact formular request 

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 if the contact request e-mail can be send
    """
    # Get the recipient and subject from the request
    sender = request.POST.get('from')
    email = request.POST.get('email')
    message = request.POST.get('message')


    # Render the email message body using the email.html template
    text_message = render_to_string('contact.html', {
        'subject': 'Neue Kontaktanfrage',
        'sender': sender,
        'email':email,
        'message':message,
    })

    # Create the EmailMessage object and send the email
    email = EmailMessage(
        subject='Kontaktanfrage',
        body=text_message,
        #NEEDS TO BE ADAPTED TO BE REMOVED FOR COMPANIES
        from_email='its.kompetent@uni-goettingen.de',
        to=['its.kompetent@uni-goettingen.de']
    )
    email.content_subtype = 'html'
    email.send()

    return JsonResponse({'success': True})

@api_view(['POST'])
def generate_individual_report(request):
    """
    Generates an individual report that summarizes the  results from the taken competence test of a participant

    Args:
        request (HttpRequest): A Django HttpRequest object containing the HTTP request information.

    Returns:
        Response: A Django Response object. 
        - Returns a success message and status 200 including the PDF blob object.
    """
    try:
        competence_test_result= json.loads(request.body.decode('utf-8'))
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    

    competence_dimension_scores = competence_test_result['competenceDimensionScore']
    total_points_scored = competence_test_result['totalPointsScored']
    test_situations= competence_test_result['test_situations']
    job_profile_id = competence_test_result['job_profile_id']
    selected_job_profile =  JobProfile.objects.get(id=job_profile_id)
    job_profiles = list(JobProfile.objects.all())
    competence_dimensions = list(CompetenceDimension.objects.all())
    number_of_threats = len(test_situations)

    threats = []
    competence_dimensions_per_threat = []
    competence_dimension_scores_per_threat = []
    competence_bar_charts_per_threat = []

    for threat_situation in test_situations:
        threats.append({'threat_vector_name': threat_situation['threat_vector']['threatVectorText'], 'threat_vector_description': threat_situation['threat_vector']['threat_vector_description'], 'score': round(threat_situation['pointsScored']/14*100)})
        for test_item in threat_situation['threat_vector']['test_items']:
            competence_dimensions_per_threat.append(test_item['competence_dimension']['dimension_name'])
            competence_dimension_scores_per_threat.append(round(test_item['question_item'][0]['points']/2 * 100))


        competence_bar_charts_per_threat.append({'chart': generate_competence_bar_chart_per_threat(competence_dimensions_per_threat, competence_dimension_scores_per_threat), 'threat_vector_name': threat_situation['threat_vector']['threatVectorText'], 'threat_vector_description': threat_situation['threat_vector']['threat_vector_description'], 'score': round(threat_situation['pointsScored']/14*100)})
        competence_dimension_scores_per_threat = []
        competence_dimensions_per_threat = []


    threat_chart = generate_threat_chart(test_situations, total_points_scored)


    competence_bar_chart = generate_competence_bar_chart(competence_dimension_scores, test_situations)

    context = {
        'competence_bar_chart':competence_bar_chart,
        'threat_chart': threat_chart,
        'competence_dimensions':competence_dimensions,
        'selected_job_profile':selected_job_profile,
        'job_profiles':job_profiles,
        'threats':threats,
        'competence_bar_charts_per_threat':competence_bar_charts_per_threat,
        'number_of_threats':number_of_threats,

    }


    html_string = render_to_string('individual_report.html', context)
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="individual_report.pdf"'
    HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf(response)
    return response
    
    




