from django.db import models
import uuid
from job_profiles.models import JobProfile
from threats.models import ThreatSituation, ThreatVector
from competence_tests.models import CompetenceDimension
from django.core.validators import MinValueValidator

class CompetenceDimensionScorePerThreat(models.Model):
    """
    Represents a model to store the aggregated scored points for each competence dimension to a specific security threat.

    Attributes:
        competence_dimension (ForeinKey): The associated competence dimension
        scoredPoints (IntegerField): An integer for the score that gets counted up
    """
    competence_dimension = models.ForeignKey(CompetenceDimension, on_delete=models.CASCADE)
    scoredPoints = models.IntegerField()  

class CompetenceDimensionScore(models.Model):
    """
    Represents a model to store the aggregated scored points for each competence dimensions over all security threats.

    Attributes:
        competence_dimension (ForeinKey): The associated competence dimension
        scoredPoints (IntegerField): An integer for the score that gets counted up
    """
    competence_dimension = models.ForeignKey(CompetenceDimension, on_delete=models.CASCADE)
    scoredPoints = models.IntegerField()  

class ThreatSituationScore(models.Model):
    """
    Represents a model to store the aggregated scored points for each competence dimensions over all security threats.

    Attributes:
        related_competence_dimension_scores (ManyToManyField): Represents the score for each competence dimension for the specific security threat
        threat_situation (ForeinKey): The ThreatSituation associated to The ThreatSituationScore
        threat_vector (ForeignKey): The ThreatVector associated to The ThreatSituationScore
        scoredPoints (IntegerField): An integer for the score that gets counted up
    """
    related_competence_dimension_scores = models.ManyToManyField(CompetenceDimensionScorePerThreat)
    threat_situation = models.ForeignKey(ThreatSituation, on_delete=models.CASCADE)
    threat_vector = models.ForeignKey(ThreatVector, on_delete=models.CASCADE)
    scoredPoints = models.IntegerField()  

class Invitation(models.Model):
    """
    Represents an invitation to participate in a campagne, uniquely identified by a token.

    Attributes:
        token (UUIDField): A unique identifier for the invitation, generated automatically.
        email_encrypted (CharField): The encrypted email address of the invitee.
        is_participated (BooleanField): Indicates whether the invitee has participated.
        created_by (ForeignKey to User): The user who created the invitation.
        date_created (DateTimeField): The date and time when the invitation was created, set automatically.
        reusable (BooleanField): Indicates whether the invitation can be used more than once.
        usage_active (BooleanField): Indicates whether the  invitation tokens are still valid (false when user ends campaign)
        tokenCounter (IntegerField): Counts how many times the token has been used.
    """
    token = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    email_encrypted = models.CharField(max_length=255)
    is_participated = models.BooleanField(default=False)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    reusable = models.BooleanField(default=False)
    usage_active = models.BooleanField(default=True)
    tokenCounter = models.IntegerField(default=0)  



class Campagne(models.Model):
    """
    Represents a campagne created by a user to invite participants.

    Attributes:
        created_by (OneToOneField to User): The user who created the campagne.
        date_created (DateTimeField): The date and time when the campagne was created, set automatically.
        one_token_mode (BooleanField): Specifies the token mode for the campagne; `None` if not set, `True` for a single use token, `False` for multiple use tokens.
        security_key_activated (BooleanField): Indicates whether a security key is activated for the campagne.
        security_display_threshold (IntegerField): A security threshold that makes  sure data only get aggregated when at least 5 participants.
        aggregate_over_single_profiles (BooleanField): Indicates whether aggregation mode over single profiles is active.
        campaign_ended (BooleanField): Indicates whether the campaign has been ended by the campagne manager


    """
    created_by = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    # none if not set, true for one invitation code, false for multiple invitation codes
    one_token_mode = models.BooleanField(null=True)
    security_key_activated = models.BooleanField(default=True)
    security_display_threshold = models.IntegerField(default= 5, validators=[
        MinValueValidator(5)
    ], verbose_name="Minimum Teilnehmende für die Datenaggregation")
    aggregate_over_single_profiles= models.BooleanField(default=True)
    campaign_ended = models.BooleanField(default=False)


    def save(self, *args, **kwargs):
        # Ensure validation is performed before saving
        self.full_clean()
        super().save(*args, **kwargs)

class CompetenceTestResult(models.Model):
    """
    Stores the results of a competence test taken by a user, including scores in various dimensions.

    Attributes:
        created_by (ForeignKey to User): The user who took the test.
        job_profile (ForeignKey to JobProfile): The job profile associated with the test.
        threat_situation_score (ManyToManyField to ThreatSituationScore): Scores related to threat situations assessed in the test.
        competence_dimension_score (ManyToManyField to CompetenceDimensionScore): Scores across different competence dimensions evaluated in the test.
    """
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    job_profile = models.ForeignKey(JobProfile, on_delete=models.CASCADE)
    threat_situation_score = models.ManyToManyField(ThreatSituationScore)
    competence_dimension_score = models.ManyToManyField(CompetenceDimensionScore)



