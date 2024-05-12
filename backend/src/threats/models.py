from django.db import models
from job_profiles.models import JobProfile
# Create your models here.

class ThreatEvent(models.Model):
    """
    Represents a model to store the threat events

    Attributes:
        event_name (CharField): The name of the threat event
        event_desciption (TextField): A description of the meaning of the threat event

    Returns:
        (str): The threat event name for the admin interface
    """
    event_name = models.CharField(max_length=140, verbose_name='Bezeichnung')
    event_description = models.TextField(null=True, verbose_name='Beschreibung')

    class Meta:
        verbose_name = "Bedrohungsereignis"
        verbose_name_plural = "Bedrohungsereignisse"

    def __str__(self):
        return self.event_name


class ThreatArea(models.Model):
    """
    Represents a model to store the threat area

    Attributes:
        are_name (CharField): The name of the threat area
        area_desciption (TextField): A description of the meaning of the threat area

    Returns:
        (str): The threat area name for the admin interface
    """
    area_name = models.CharField(max_length=140, verbose_name='Bezeichnung')
    area_description = models.TextField(null=True, verbose_name='Beschreibung')

    class Meta:
        verbose_name = "Bedrohungsbereich"
        verbose_name_plural = "Bedrohungsbereiche"

    def __str__(self):
        return self.area_name

class ThreatVector(models.Model):
    """
    Represents a model to store the threat vectors. A threat vector is composed of a threat event and a threat area

    Attributes:
        threat_event (ForeinKey): The associated threat event
        threat_area(ForeinKey): The associated threat area
        threat_vector_description (TextField): A description of the threat vector 

    Returns:
        (str): The threat vector name for the admin interface
    """
    threat_event = models.ForeignKey(ThreatEvent, on_delete=models.CASCADE, verbose_name='Zugeordnetes Bedrohungsereignis')
    threat_area = models.ForeignKey(ThreatArea, on_delete=models.CASCADE, verbose_name='Zugeordneter Bedrohungsbereich')
    threat_vector_description = models.TextField(null=True, verbose_name='Beschreibung')


    class Meta:
        verbose_name = "Bedrohungsvektor"
        verbose_name_plural = "Bedrohungsvektoren"

    def __str__(self):
        return self.threat_event.event_name+ "/" + self.threat_area.area_name


class ThreatSituation(models.Model):
    """
    Represents a model to store the threat situations. A threat situation is related to one specific threat vector.

    Attributes:
        threat_description (TextField): The associated threat event
        threat_vector (ForeinKey): The associated threat vector
        job_profile (ForeinKey): The associated job profile

    Returns:
        (str): The threat situation description composed of threat event and threat area name as well as job profile name for the admin interface
    """
    threat_situation_identificator = models.CharField(max_length=140, verbose_name='Kennung', null=True, blank=True)
    threat_description = models.TextField(null=True, verbose_name='Beschreibung')
    threat_vector = models.ForeignKey(ThreatVector, null=True, on_delete=models.CASCADE, verbose_name='Zugeordneter Bedrohungsvektor')
    # remove null = True
    job_profile = models.ForeignKey(JobProfile, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Zugeordnetes Anforderungsprofil')


    class Meta:
        verbose_name = "Bedrohungssituation"
        verbose_name_plural = "Bedrohungssituationen"

    def __str__(self):
        return str(self.threat_situation_identificator) + "/"+ self.threat_vector.threat_event.event_name + "/" + self.threat_vector.threat_area.area_name + "/" + self.job_profile.job_name
