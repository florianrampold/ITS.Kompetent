from django.db import models
from threats.models import ThreatVector
from threats.models import ThreatSituation
from polymorphic.models import PolymorphicModel
from job_profiles.models import JobProfile
from competence_tests.choices import *


class CompetenceDimension(models.Model):
    """
    Represents a model to store the competence dimensions.

    Attributes:
        dimension_name (CharField): The name of the competence dimension
        dimension_desciption (TextField): A description of the meaning of the competence dimension

    Returns:
        (str): The dimension name for the admin interface
    """
    dimension_name = models.CharField(max_length=140, verbose_name='Kompetenzdimension')
    dimension_description= models.TextField(null=True, verbose_name='Beschreibung der Kompetenzdimension')

    class Meta:
        verbose_name = "Kompetenzdimension"
        verbose_name_plural = "Kompetenzdimensionen"


    def __str__(self):
        return self.dimension_name
        
class QuestionItem(models.Model):
    """
    Represents a model to store one question for each competence dimension associated to a threat vector and threat situation.

    Attributes:
        question_name (CharField): A unique identifier for the question which needs to be set by the admin
        question (TextField): A description of question
        type (IntegerField): Specifies the type of the question (single-choice, multiple choice, ranking)

    Returns:
        (str): The identifier of the question
    """
    question_name = models.CharField(max_length=140, null=True, verbose_name='Name der Frage')
    question = models.TextField(null=True, verbose_name='Text zur Frage')
    type = models.IntegerField(choices=CHOICES_FIELD, default=1, verbose_name='Fragen-Typ')   

    class Meta:
        verbose_name = "Frage"
        verbose_name_plural = "Fragen"

    def __str__(self):
        return self.question_name

class Impulse(PolymorphicModel):
    """
    Represents a polymorphic model to store impulses used to test the competence dimension Threat Awareness

    Attributes:
        impulse_name (CharField): The name of the impulse

    Returns:
        (str): The impulse name for the admin interface
    """
    impulse_name = models.CharField(max_length=140, null=True, verbose_name='Name des Impulses')

    class Meta:
        verbose_name = "Impuls"
        verbose_name_plural = "Impulse"

    def __str__(self):
        return self.impulse_name


class ImageItem(models.Model):
    """
    Represents a model to store images for ImageImpulses.

    Attributes:
        image_name (CharField): The name of the image
        image_field (ImageField): The file for image upload
        image_description (TextField): A description of the image (optional)

    Returns:
        (str): The image name for the admin interface
    """
    image_name = models.CharField(max_length=140, null=True, verbose_name='Kennung des Bildes')
    image_field = models.ImageField(upload_to ='static/images', verbose_name='Bild-Datei')
    image_description = models.TextField(null=True, blank=True, verbose_name='Text zur Bild-Datei')


    class Meta:
        verbose_name = "Bild"
        verbose_name_plural = "Bilder"

    def __str__(self):
        return self.image_name


class EmailItem(models.Model):
    """
    Represents a model to store e-mails for EmailImpulses. This model includes detailed
    information about the e-mail, such as sender, recipient, subject (regarding), teaser, and content,
    as well as associated metadata like the sender's image and the e-mail's date. 

    Attributes:
        email_name (CharField): The identifier or name of the e-mail, used for reference or management purposes.
        email_sender (CharField): The sender's name or e-mail address.
        email_recipient (CharField): The recipient's name or e-mail address.
        email_regarding (CharField): The subject line of the e-mail.
        email_teaser (TextField): A short preview or teaser of the e-mail content, shown before opening the e-mail.
        email_content (TextField): The full content of the e-mail.
        email_image_sender (ImageField): An optional image representing the sender, which can be displayed in the e-mail.
        email_date (TimeField): The date and time the e-mail is meant to represent or be sent.
        email_button_text (CharField): Optional text for a call-to-action button within the e-mail.

    The model also specifies verbose names for itself and its fields to enhance readability and
    management in the Django admin interface.
    """
    email_name= models.CharField(max_length=140, null=True, verbose_name='Kennung der E-Mail')
    email_sender= models.CharField(max_length=140, null=True, verbose_name='Sender der E-Mail')
    email_recipient = models.CharField(max_length=140, null=True, verbose_name='Empfänger der E-Mail')
    email_regarding = models.CharField(max_length=140, null=True, verbose_name='Betreff')
    email_teaser = models.TextField(null=True, verbose_name='Vorschau')
    email_content = models.TextField(null=True, verbose_name='Inhalt')
    email_image_sender = models.ImageField(null=True, blank=True, upload_to ='static/images', verbose_name='Bild des Senders')
    email_date = models.TimeField(verbose_name='Datum der E-Mail')
    email_is_signed_image= models.ImageField(null=True, blank=True, upload_to ='static/images', verbose_name='Bild zur Signatur')

   # email_button_text = models.CharField(max_length=140, blank=True, verbose_name='Text für Button')

    class Meta:
        verbose_name = "E-Mail"
        verbose_name_plural = "E-Mails"

    def __str__(self):
        return self.email_name

class EmailImpulse(Impulse):
    """
    Represents a model to store EmailImpulses, where many emails can be related to. 

    Attributes:
        email (ManyToManyField): EmailItems that are related to this class of Impulse
        impulse_text (CharField): The specific text that is related to an EmailImpulse, appears under the text for the threat situation.

    """
    email =models.ManyToManyField(EmailItem, verbose_name='E-Mail')
    impulse_text = models.CharField(max_length=800, null=True, blank=True, verbose_name='Text zum Impuls')


    class Meta:
        verbose_name = "E-Mail Impuls"
        verbose_name_plural = "E-Mail Impulse"


class ImageImpulse(Impulse):
    """
    Represents a model to store ImageImpulses, where many images (usually three) can be related to. 

    Attributes:
        email (ManyToManyField): EmailItems that are related to this class of Impulse
        impulse_text (CharField): The specific text that is related to an ImageImpulse, appears under the text for the threat situation.

    """
    image =models.ManyToManyField(ImageItem, verbose_name='Bild')
    impulse_text = models.TextField(null=True, blank=True, verbose_name='Text zum Impuls')


    class Meta:
        verbose_name = "Bild Impuls"
        verbose_name_plural = "Bild Impulse"

class ChatInterface(models.Model):
    """
    Represents a model to store chats for ChatImpulses. This model includes detailed
    information about the chat, such as sender, an image of the sender and incoming and outgoing messages.

    Attributes:
        chat_sender_name (CharField): The identifier or name of chat sender
        chat_sender_known (BooleanField): Specifies if the sender of the message shoud be known to the recipient
        chat_sender_image (ImageField): The file for an image of the sender (optional)
        chat_message_incoming (CharField): The first incoming message by the sender
        chat_message_incoming_date (TextField): The date of the first incoming message of the sender.
        chat_message_outgoing (TextField): The reply of the recipient of the message (optional).
        chat_message_outgoing_date (TimeField): The date of the first outgoing message of the recipient.
        chat_message_incoming_2 (TextField): The second incoming message by the sender (optional).
        chat_message_incoming_date_2 (DateField): The date of the second outgoing message of the recipient.

    The model also specifies verbose names for itself and its fields to enhance readability and
    management in the Django admin interface.
    """
    chat_sender_name = models.CharField(max_length=140, verbose_name='Name des Senders')
    chat_sender_known = models.BooleanField(default=False, null=True, verbose_name='Absender bekannt')
    chat_sender_image = models.ImageField(upload_to ='static/images', blank=True, verbose_name='Bild des Senders')
    chat_message_incoming =models.TextField(verbose_name='Eingehende Nachricht 1')
    #why TimeField?
    chat_message_incoming_date = models.TimeField(verbose_name='Datum der 1. eingehenden Nachricht')
    chat_message_outgoing =models.TextField(max_length=800, blank=True, verbose_name='Ausgehende Nachricht (optional)')
    chat_message_outgoing_date = models.TimeField(blank=True, null=True, verbose_name='Datum der ausgehenden Nachricht (optional)')
    chat_message_incoming_2 =models.TextField(max_length=800, blank=True, verbose_name='Eingehende Nachricht 2 (optional)')
    chat_message_incoming_date_2 = models.DateField(blank=True, null=True, verbose_name='Datum der 2. eingehenden Nachricht (optional)')

    class Meta:
        verbose_name = "Chat Interface"
        verbose_name_plural = "Chat Interfaces"
    
  

class ChatImpulse(Impulse):
    """
    Represents a model to store ChatImpulses, where many chats (usually three) can be related to. 

    Attributes:
        chat_interface (ManyToManyField): Chats that are related to this class of Impulse
        impulse_text (CharField): The specific text that is related to an ChatImpulse, appears under the text for the threat situation.

    """
    chat_interface =models.ManyToManyField(ChatInterface, verbose_name='Chat Interface')
    impulse_text = models.TextField(null=True, blank=True, verbose_name='Text zum Impuls')


    class Meta:
        verbose_name = "Chat Impuls"
        verbose_name_plural = "Chat Impulse" 
#rename
class CompetenceTestItem(models.Model):
    """
    Represents a model to store CompetenceTestItems. A CompetenceTestItem represents a test scenario that includes a competence dimension and a related question. An impulse can be related but should only be applied if he competence dimension is Threat Awareness. 

    Attributes:
        question_item (ManyToManyField): The questions that are related to a CompetenceTestItem (usually one). 
        impulse_item (ForeignKey): The related Impulse (EmailImpulse, ImageImpulse or ChatImpulse)
        threat_situation (ForeignKey): The related threat situation
        competence_dimension (ForeignKey): The related competence dimension

    """
    #many to many? --> needs to be changed
    question_item = models.ManyToManyField(QuestionItem, blank=True, verbose_name='Zugeordnete Frage')
    impulse_item = models.ForeignKey(Impulse, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Zugeordneter Impuls')
    threat_situation =models.ForeignKey(ThreatSituation, on_delete=models.CASCADE, verbose_name='Zugeordnete Bedrohungssituation')
    competence_dimension=models.ForeignKey(CompetenceDimension, on_delete=models.CASCADE, verbose_name='Zugeordnete Kompetenzdimension')

    class Meta:
        verbose_name = "Kompetenztest Szenario"
        verbose_name_plural = "Kompetenztest Szenarios"

    def __str__(self):
        return self.threat_situation.threat_vector.threat_event.event_name+ "/" + self.threat_situation.threat_vector.threat_area.area_name + "/" + self.competence_dimension.dimension_name + "/" + self.threat_situation.job_profile.job_name


class ChoiceItem(models.Model):
    """
    Represents a model to store AnswerOptions to a specific question.

    Attributes:
        question (ForeignKey): The related question. Each question can have multiple ChoiceItems.
        option (TextField): The answer option
        answer_rating (IntegerField): The rating of the given answer by the user (0, 1 or 2 where 2 is best)

    """
    question = models.ForeignKey(QuestionItem, on_delete=models.CASCADE, verbose_name='Zugeordnete Frage',related_name="questionn")
    option = models.TextField(verbose_name='Antwortoption')
    answer_rating = models.IntegerField(choices=ANSWER_RATING, default=0, verbose_name='Bewertung der Antwortoption')  

    class Meta:
        verbose_name = "Antwort"
        verbose_name_plural = "Antworten"
        ordering = ['question']

    def __str__(self):
        return self.question.question_name 


class CompetenceTest(models.Model):
    """
    Represents a model to assign job profiles and threat vectors to a competence test. There should exist one CompetenceTest for each JobProfile.

    Attributes:
        job_profile (OneToOneField): The job profile associated with the competence test
        threat_vector (ManyToManyField): 

    """
    job_profile = models.OneToOneField(JobProfile, on_delete=models.CASCADE, verbose_name='Zugeordnetes Anforderungsprofil')
    # needs to be changed to threat situation
    threat_situations = models.ManyToManyField(
        ThreatSituation,
        verbose_name='Zugeordnete Bedrohungssituationen'
    )
    #threat_vector =models.ManyToManyField(ThreatVector, verbose_name='Zugeordnete Bedrohungsvektoren')

    class Meta:
        verbose_name = "Kompetenztest"
        verbose_name_plural = "Kompetenztests"

    def __str__(self):
        return self.job_profile.job_name
 