from django.db import models
from competence_tests.models import CompetenceDimension
from threats.models import ThreatEvent
from trainings.choices import *


class TargetAudience(models.Model):
    """
    Represents a model to store the target audience of a training.

    Attributes:
        audience_name (CharField): The name of the audience
       

    Returns:
        (str): The audience name for the admin interface
    """
    audience_name = models.CharField(max_length=140, verbose_name='Zielgruppenbezeichnung')

    class Meta:
        verbose_name = "Zielgruppe"
        verbose_name_plural = "Zielgruppen"

    def __str__(self):
        return self.audience_name

class DeliveryMethod(models.Model):
    """
    Represents a model to store the devlivery methods of a training.

    Attributes:
        delivery_method (CharField): The name of the delivery method
       

    Returns:
        (str): The delivery method for the admin interface
    """
    delivery_method = models.CharField(max_length=140, verbose_name='Vermittlungsmethode')


    class Meta:
        verbose_name = "Vermittlungsmethode"
        verbose_name_plural = "Vermittlungsmethoden"

    def __str__(self):
        return self.delivery_method

class Language(models.Model):
    """
    Represents a model to store the languages that are applicable for a training.

    Attributes:
        language (CharField): The name of the language
       

    Returns:
        (str): The language for the admin interface
    """
    language = models.CharField(max_length=140, verbose_name='Sprache')


    class Meta:
        verbose_name = "Sprache des Trainings"
        verbose_name_plural = "Sprache der Trainings"

    def __str__(self):
        return self.language

class TrainingGroup(models.Model):
    """
    Represents a model to store the training group of a training. Trainings are goruped by a training group so that no training with equal importanc ebased on the competence test result gets preferred.

    Attributes:
        identifier (CharField): The identifier of the training
       

    Returns:
        (str): The identifier for the admin interface
    """
    identifier= models.CharField(max_length=140, null=True, verbose_name='Identifizierung der Gruppe')


    class Meta:
        verbose_name = "Trainings-Gruppe"
        verbose_name_plural = "Trainings-Gruppen"

    def __str__(self):
        return self.identifier

class Training(models.Model):
    """
    Represents a model to store the trainings.

    Attributes:
        training_group (ForeinKey): The name of the audience
        training_provider (CharField): The provider of the training
        training_name (CharField): The name of the training
        delivery_method (ManyToManyField): One or many delivery methods that can be chosen by the admin
        costs (IntegerField): The costs of participating in a training
        certification (IntegerField): Defines whether participants get a certficate after participating
        language (ManyToManyField): The languages that are applicable in the training
        competence_dimensions (ManyToManyField): The competence dimensions that are covered by the training program
        threat_event (ManyToManyField): The threat events that are covered by the training program
        training_url (URLField): The link to the website of the training provider
       

    Returns:
        (str): The name of the training
    """
    training_group = models.ForeignKey(TrainingGroup, null=True, on_delete=models.CASCADE, verbose_name="Zugeordnete Trainings-Gruppe")
    training_provider = models.CharField(max_length=140, null=True, verbose_name='Anbieter')
    training_name = models.CharField(max_length=140, verbose_name='Bezeichnung')
    delivery_method =models.ManyToManyField(DeliveryMethod, verbose_name='Zugeordnete Vermittlungsmethode')
    costs = models.IntegerField(choices=COSTS_CHOICES, default=1, verbose_name='Kosten')
    certification = models.IntegerField(choices=CERTIFICATE_CHOICES, default=1, verbose_name='Zertifizierung')
    language =models.ManyToManyField(Language, verbose_name='Zugeordnete Sprache')
    competence_dimensions =models.ManyToManyField(CompetenceDimension, blank= True, related_name = 'competence_dimensions', verbose_name='Zugeordnete Kompetenzdimensionen')
    threat_event =models.ManyToManyField(ThreatEvent, blank=True, verbose_name='Zugeordnete Bedrohungsereignisse')
    training_url = models.URLField(max_length=400, null = True, verbose_name='Link')


    class Meta:
        verbose_name = "SETA Programm"
        verbose_name_plural = "SETA Programme"

    def __str__(self):
        return self.training_name


