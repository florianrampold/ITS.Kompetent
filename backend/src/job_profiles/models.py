from django.db import models

class JobProfile(models.Model):
    """
    Represents a model to store the job profiles

    Attributes:
        job_name (CharField): The name of the competence dimension
        job_desciption (TextField): A description of the meaning of the competence dimension
        job_tasks (TextField): The common tasks related to the job profile
        show_job_profile (BooleanField): A boolean field that allows to display the job profile in the frontend or to hide it.

    Returns:
        (str): The dimension name for the admin interface
    """
    job_name = models.CharField(max_length=140, verbose_name='Bezeichnung')
    job_description = models.TextField(verbose_name='Beschreibung')
    job_tasks = models.TextField(null=True, verbose_name='Tätigkeiten')
    show_job_profile = models.BooleanField(default=False, verbose_name='Anzeigen')

    class Meta:
        ordering = ['job_name']
        verbose_name = "Anforderungsprofil"
        verbose_name_plural = "Anforderungsprofile"

    def __str__(self):
        return self.job_name



 