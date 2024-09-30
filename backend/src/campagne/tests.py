from django.test import TestCase
from campagne.models import *
from competence_tests.models import *
from threats.models import *
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from django.middleware.csrf import get_token
import json
from uuid import UUID

class CompetenceDimensionScorePerThreatTestCase(TestCase):

    def setUp(self):
        self.competence_dimension = CompetenceDimension.objects.create(dimension_name="Threat Awareness")

        self.score_per_threat = CompetenceDimensionScorePerThreat.objects.create(
            competence_dimension=self.competence_dimension,
            scoredPoints=7
        )

    def test_create_competence_dimension_score_per_threat(self):
        """Test creating a CompetenceDimensionScorePerThreat object."""
        score_per_threat = CompetenceDimensionScorePerThreat.objects.create(
            competence_dimension=self.competence_dimension,
            scoredPoints=7
        )
        self.assertIsNotNone(score_per_threat.id)
        self.assertEqual(score_per_threat.competence_dimension, self.competence_dimension)
        self.assertEqual(score_per_threat.scoredPoints, 7)

    def test_read_competence_dimension_score_per_threat(self):
        """Test retrieving a CompetenceDimensionScorePerThreat object."""
        score_per_threat = CompetenceDimensionScorePerThreat.objects.get(id=self.score_per_threat.id)
        self.assertEqual(score_per_threat.competence_dimension, self.competence_dimension)
        self.assertEqual(score_per_threat.scoredPoints, 7)

    def test_update_competence_dimension_score_per_threat(self):
        """Test updating a CompetenceDimensionScorePerThreat object."""
        self.score_per_threat.scoredPoints = 5
        self.score_per_threat.save()

        updated_score_per_threat = CompetenceDimensionScorePerThreat.objects.get(id=self.score_per_threat.id)
        self.assertEqual(updated_score_per_threat.scoredPoints, 5)

    def test_delete_competence_dimension_score_per_threat(self):
        """Test deleting a CompetenceDimensionScorePerThreat object."""
        score_per_threat_id = self.score_per_threat.id
        self.score_per_threat.delete()

        with self.assertRaises(CompetenceDimensionScorePerThreat.DoesNotExist):
            CompetenceDimensionScorePerThreat.objects.get(id=score_per_threat_id)


class CompetenceDimensionScoreTestCase(TestCase):

    def setUp(self):
        self.competence_dimension = CompetenceDimension.objects.create(dimension_name="Threat Awareness")

        self.score = CompetenceDimensionScore.objects.create(
            competence_dimension=self.competence_dimension,
            scoredPoints=2
        )

    def test_create_competence_dimension_score(self):
        """Test creating a CompetenceDimensionScore object."""
        score = CompetenceDimensionScore.objects.create(
            competence_dimension=self.competence_dimension,
            scoredPoints=2
        )
        self.assertIsNotNone(score.id)
        self.assertEqual(score.competence_dimension, self.competence_dimension)
        self.assertEqual(score.scoredPoints, 2)

    def test_read_competence_dimension_score(self):
        """Test retrieving a CompetenceDimensionScore object."""
        score = CompetenceDimensionScore.objects.get(id=self.score.id)
        self.assertEqual(score.competence_dimension, self.competence_dimension)
        self.assertEqual(score.scoredPoints, 2)

    def test_update_competence_dimension_score(self):
        """Test updating a CompetenceDimensionScore object."""
        self.score.scoredPoints = 1
        self.score.save()

        updated_score = CompetenceDimensionScore.objects.get(id=self.score.id)
        self.assertEqual(updated_score.scoredPoints, 1)

    def test_delete_competence_dimension_score(self):
        """Test deleting a CompetenceDimensionScore object."""
        score_id = self.score.id
        self.score.delete()

        with self.assertRaises(CompetenceDimensionScore.DoesNotExist):
            CompetenceDimensionScore.objects.get(id=score_id)


class ThreatSituationScoreTestCase(TestCase):

    def setUp(self):
        self.threat_event = ThreatEvent.objects.create(
            event_name="Phishing", 
            event_description="A phishing threat event"
        )
        self.threat_area = ThreatArea.objects.create(
            area_name="Mailsystem", 
            area_description="A Mailsystem"
        )

        self.threat_vector = ThreatVector.objects.create(
            threat_event=self.threat_event, 
            threat_area=self.threat_area,
            threat_vector_description="Phishing over Mailsystem"
        )
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation"
        )

        self.competence_dimension_1 = CompetenceDimension.objects.create(dimension_name="Threat Awareness")
        self.competence_dimension_2 = CompetenceDimension.objects.create(dimension_name="Threat Identification")

        self.competence_dimension_score_1 = CompetenceDimensionScorePerThreat.objects.create(
            competence_dimension=self.competence_dimension_1,
            scoredPoints=2
        )
        self.competence_dimension_score_2 = CompetenceDimensionScorePerThreat.objects.create(
            competence_dimension=self.competence_dimension_2,
            scoredPoints=1
        )

        self.threat_situation_score = ThreatSituationScore.objects.create(
            threat_situation=self.threat_situation,
            threat_vector=self.threat_vector,
            scoredPoints=3
        )
        self.threat_situation_score.related_competence_dimension_scores.set(
            [self.competence_dimension_score_1, self.competence_dimension_score_2]
        )

    def test_create_threat_situation_score(self):
        """Test creating a ThreatSituationScore object."""
        new_threat_situation_score = ThreatSituationScore.objects.create(
            threat_situation=self.threat_situation,
            threat_vector=self.threat_vector,
            scoredPoints=3
        )
        new_threat_situation_score.related_competence_dimension_scores.set(
            [self.competence_dimension_score_1]
        )
        self.assertIsNotNone(new_threat_situation_score.id)
        self.assertEqual(new_threat_situation_score.scoredPoints, 3)
        self.assertEqual(new_threat_situation_score.related_competence_dimension_scores.count(), 1)

    def test_read_threat_situation_score(self):
        """Test retrieving a ThreatSituationScore object."""
        threat_situation_score = ThreatSituationScore.objects.get(id=self.threat_situation_score.id)
        self.assertEqual(threat_situation_score.scoredPoints, 3)
        self.assertEqual(threat_situation_score.related_competence_dimension_scores.count(), 2)

    def test_update_threat_situation_score(self):
        """Test updating a ThreatSituationScore object."""
        self.threat_situation_score.scoredPoints = 4
        self.threat_situation_score.save()

        updated_score = ThreatSituationScore.objects.get(id=self.threat_situation_score.id)
        self.assertEqual(updated_score.scoredPoints, 4)

        self.threat_situation_score.related_competence_dimension_scores.set([self.competence_dimension_score_2])
        self.assertEqual(self.threat_situation_score.related_competence_dimension_scores.count(), 1)

    def test_delete_threat_situation_score(self):
        """Test deleting a ThreatSituationScore object."""
        score_id = self.threat_situation_score.id
        self.threat_situation_score.delete()

        with self.assertRaises(ThreatSituationScore.DoesNotExist):
            ThreatSituationScore.objects.get(id=score_id)



class InvitationAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.client.login(username='testuser', password='testpass')

        self.campagne = Campagne.objects.create(
            created_by=self.user,
            one_token_mode=False,
            security_key_activated=False,
            security_display_threshold=5,
            aggregate_over_single_profiles=True,
            campaign_ended=False
        )

        self.invitation_1 = Invitation.objects.create(
            email_encrypted="encryptedemail1@example.com",
            is_participated=False,
            created_by=self.user,
            reusable=True,
            usage_active=True,
            tokenCounter=0,
            token='f5022aa4-39a6-4921-a691-a14384cfcc9f',
        )
        self.invitation_2 = Invitation.objects.create(
            email_encrypted="encryptedemail2@example.com",
            is_participated=True,
            created_by=self.user,
            reusable=False,
            usage_active=False,
            tokenCounter=1,
            token='e9b1d59d-3f5b-4d68-9a79-8c2cfc04a2b2',
        )

        self.get_invitations_url = reverse('get_invitations')
        self.create_invitations_url = reverse('create_invitations')
        self.invalidate_invitation_tokens_url = reverse('invalidate_invitation_tokens')
    def test_validate_invitation_token_valid(self):
        """Test validating a valid invitation token."""
        valid_token = str(self.invitation_1.token)  
        response = self.client.get(reverse('invitation_token', args=[valid_token]))  
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'valid': True})

    def test_validate_invitation_token_invalid(self):
        """Test validating an invalid UUID token."""
        invalid_token = 'invalid-uuid-token'
        response = self.client.get(reverse('invitation_token', args=[invalid_token]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'valid': False})

    def test_validate_invitation_token_nonexistent(self):
        """Test validating a nonexistent invitation token."""
        nonexistent_token = str(UUID('c607d7e4-b80b-4cf8-abc8-56c1eada645f'))
        response = self.client.get(reverse('invitation_token', args=[nonexistent_token]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'valid': False})

    def test_validate_invitation_token_already_used(self):
        """Test validating a token that has been used or is inactive."""
        response = self.client.get(reverse('invitation_token', args=[self.invitation_2.token]))        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {'valid': False})

    def test_invalidate_invitation_tokens_success(self):
        """Test invalidating the user's invitation tokens successfully."""
        self.client.force_login(self.user)

        csrf_token = get_token(self.client.get(self.invalidate_invitation_tokens_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)

        response = self.client.put(self.invalidate_invitation_tokens_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Invitations changed'})

        self.invitation_1.refresh_from_db()
        self.invitation_2.refresh_from_db()


    def test_invalidate_invitation_tokens_no_invitations_found(self):
        """Test invalidating tokens when the user has no invitations."""
        new_user = User.objects.create_user(username='newuser', password='newpass')
       
        self.client.force_login(new_user)

        csrf_token = get_token(self.client.get(self.invalidate_invitation_tokens_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)

        response = self.client.put(self.invalidate_invitation_tokens_url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Invitation not found'})

    def test_get_invitations(self):
        """Test retrieving a list of invitations."""
        response = self.client.get(self.get_invitations_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        sorted_data = sorted(response.data, key=lambda x: x['email_encrypted'])

        self.assertEqual(len(sorted_data), 2)

        self.assertEqual(sorted_data[0]['email_encrypted'], 'encryptedemail1@example.com')
        self.assertEqual(sorted_data[0]['is_participated'], False)
        self.assertEqual(sorted_data[0]['created_by'], self.user.id)
        self.assertEqual(sorted_data[0]['reusable'], True)
        self.assertEqual(sorted_data[0]['usage_active'], True)
        self.assertEqual(sorted_data[0]['tokenCounter'], 0)

        self.assertEqual(sorted_data[1]['email_encrypted'], 'encryptedemail2@example.com')
        self.assertEqual(sorted_data[1]['is_participated'], True)
        self.assertEqual(sorted_data[1]['reusable'], False)
        self.assertEqual(sorted_data[1]['usage_active'], False)
        self.assertEqual(sorted_data[1]['tokenCounter'], 1)

    def test_create_invitations_with_csrf(self):
        """Test creating invitations with POST request and CSRF token."""
        self.client.force_login(self.user)

        csrf_token = get_token(self.client.get(self.create_invitations_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)

        data = {
            "emails": ["test1@example.com", "test2@example.com"],
            "key": ""
        }
        
        response = self.client.post(self.create_invitations_url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        invitations = Invitation.objects.filter(created_by=self.user)
        self.assertEqual(invitations.count(), 4)

        self.assertIn('Batch upload successful!', response.data['message'])
        self.assertEqual(len(response.data['invitations']), 2)
        self.assertEqual(response.data['invitations'][0]['email_encrypted'], 'test1@example.com')
        self.assertEqual(response.data['invitations'][1]['email_encrypted'], 'test2@example.com')



class CampagneAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.client.login(username='testuser', password='testpass')
        self.create_campagne_url = reverse('create_campagne')
        self.get_campagne_url = reverse('get_campagne')
        self.delete_campagne_url = reverse('delete_campagne')
        self.end_campagne_url = reverse('end_campaign')

    def test_create_campagne(self):
        """Test creating a Campagne with POST request."""
        self.client.force_login(self.user)

        csrf_token = get_token(self.client.get(self.create_campagne_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)
        data = {
            "oneInvitationToken": True,  
            "securityDisplayThreshold": 5,  
        }

        response = self.client.post(self.create_campagne_url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        campagne = Campagne.objects.get(created_by=self.user)
        self.assertEqual(campagne.one_token_mode, True)
        self.assertEqual(campagne.security_key_activated, True)
        self.assertEqual(campagne.security_display_threshold, 5)
        self.assertEqual(campagne.aggregate_over_single_profiles, True)
        self.assertEqual(campagne.campaign_ended, False)

    def test_end_campaign_success(self):
        """Test successfully ending a campaign."""
        self.client.force_login(self.user)
        campagne = Campagne.objects.create(
            created_by=self.user,
            one_token_mode=True,
            security_key_activated=True,
            security_display_threshold=5,
            aggregate_over_single_profiles=True,
            campaign_ended=False
        )

        csrf_token = get_token(self.client.get(self.end_campagne_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)
        data = {
            'aggregateOverSingleProfiles': False
        }
        response = self.client.put(self.end_campagne_url, data=json.dumps(data), content_type="application/json")


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {'message': 'Campagne changed'})

        campagne.refresh_from_db()

        self.assertTrue(campagne.campaign_ended)

        self.assertFalse(campagne.aggregate_over_single_profiles)
    def test_get_campagne(self):
        """Test retrieving a Campagne with GET request."""
        Campagne.objects.create(
            created_by=self.user,
            one_token_mode=True,
            security_key_activated=True,
            security_display_threshold=5,
            aggregate_over_single_profiles=True,
            campaign_ended=False
        )

        response = self.client.get(self.get_campagne_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data['one_token_mode'], True)
        self.assertEqual(response.data['security_key_activated'], True)
        self.assertEqual(response.data['security_display_threshold'], 5)
        self.assertEqual(response.data['aggregate_over_single_profiles'], True)
        self.assertEqual(response.data['campaign_ended'], False)

    def test_delete_campagne(self):
        """Test deleting a Campagne with DELETE request."""
        self.client.force_login(self.user)

        csrf_token = get_token(self.client.get(self.create_campagne_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)
        Campagne.objects.create(
            created_by=self.user,
            one_token_mode=True,
            security_key_activated=True,
            security_display_threshold=5,
            aggregate_over_single_profiles=True,
            campaign_ended=False
        )

        response = self.client.post(self.delete_campagne_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Campagne.objects.filter(created_by=self.user).exists())




class CompetenceTestResultTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

        self.client.login(username='testuser', password='testpass')
        self.create_competence_test_result_url = reverse('create_competence_test_result')
        self.job_profile = JobProfile.objects.create(id=1, job_name='backoffice Employee')

        self.get_competence_test_result_url = reverse('get_competence_test_results', args=[self.job_profile.id])

        csrf_token = get_token(self.client.get(self.create_competence_test_result_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)

        self.invitation = Invitation.objects.create(
            token='f5022aa4-39a6-4921-a691-a14384cfcc9f',
            created_by=self.user,
            reusable=True
        )

       
        self.competence_dimension_1 = CompetenceDimension.objects.create(id=1, dimension_name="Threat Awareness")
        self.competence_dimension_2 = CompetenceDimension.objects.create(id= 2, dimension_name="Threat Identification")

       
        self.threat_event = ThreatEvent.objects.create(
            event_name="Phishing", 
            event_description="A phishing threat event"
        )
        self.threat_area = ThreatArea.objects.create(
            area_name="Mailsystem", 
            area_description="A Mailsystem"
        )

        self.threat_vector = ThreatVector.objects.create(
            threat_event=self.threat_event, 
            threat_area=self.threat_area,
            threat_vector_description="Phishing over Mailsystem"
        )
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation",
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )

        self.competence_dimension_score1 = CompetenceDimensionScore.objects.create(competence_dimension=self.competence_dimension_1, scoredPoints=80)
        self.competence_dimension_score2 = CompetenceDimensionScore.objects.create(competence_dimension=self.competence_dimension_2, scoredPoints=90)

        self.cds_per_threat1 = CompetenceDimensionScorePerThreat.objects.create(
            competence_dimension=self.competence_dimension_1,
            scoredPoints=9
        )
        self.cds_per_threat2 = CompetenceDimensionScorePerThreat.objects.create(
            competence_dimension=self.competence_dimension_2,
            scoredPoints=11
        )

        self.threat_situation_score1 = ThreatSituationScore.objects.create(threat_situation=self.threat_situation, threat_vector=self.threat_vector, scoredPoints=12)
        self.threat_situation_score2 = ThreatSituationScore.objects.create(threat_situation=self.threat_situation, threat_vector=self.threat_vector, scoredPoints=8)

        self.threat_situation_score1.related_competence_dimension_scores.add(self.cds_per_threat1)
        self.threat_situation_score2.related_competence_dimension_scores.add(self.cds_per_threat2)

        competence_test_result = CompetenceTestResult.objects.create(
            created_by=self.user,
            job_profile=self.job_profile
        )

        competence_test_result.threat_situation_score.set([self.threat_situation_score1, self.threat_situation_score2])
        competence_test_result.competence_dimension_score.set([self.competence_dimension_score1, self.competence_dimension_score2])
        self.campagne = Campagne.objects.create(
            created_by=self.user,
            one_token_mode=True,
            security_key_activated=True,
            security_display_threshold=5,
            aggregate_over_single_profiles=True,
            campaign_ended=False
        )

        self.client.login(username='testuser', password='testpass')

    def test_create_competence_test_result(self):
        """
        Ensure we can create a new CompetenceTestResult object using POST.
        """
        self.client.force_login(self.user)

        csrf_token = get_token(self.client.get(self.create_competence_test_result_url).wsgi_request)

        self.client.cookies['csrfauthtoken'] = csrf_token
        self.client.credentials(HTTP_X_CSRFTOKEN=csrf_token)

        data = {
            'participant':self.invitation.token,
            'job_profile': 1,
            'threat_situation_score': [
                {
                    'related_competence_dimension_scores': [
                        {
                            'competence_dimension': 1,
                            'scoredPoints': 2
                        }
                    ],
                    'scoredPoints':4,
                    'threat_situation':self.threat_situation.id,
                    'threat_vector':self.threat_vector.id,
                },
            ],
            'competence_dimension_score': [ {'competence_dimension':1, 'scoredPoints':1}],
        }
        response = self.client.post(self.create_competence_test_result_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(CompetenceTestResult.objects.count(), 2)
        test_result = CompetenceTestResult.objects.last()
        self.assertEqual(test_result.created_by, self.user)
        self.assertEqual(test_result.job_profile, self.job_profile)
        self.assertEqual(test_result.threat_situation_score.count(), 1)
        self.assertEqual(test_result.competence_dimension_score.count(), 1)

    def test_get_competence_test_result(self):
        """
        Ensure we can retrieve a CompetenceTestResult object using GET.
        """
        self.client.force_login(self.user)

       
        headers = {
        'HTTP_ORIGIN': 'http://localhost:8080', 
        }
       
       
        response = self.client.get(self.get_competence_test_result_url, format='json', **headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CompetenceTestResult.objects.count(), 1)

    def test_get_participants_per_profile_success(self):
        """
        Test that an authenticated user can successfully fetch job profiles with participants and threat counts.
        """
        self.client.force_login(self.user)

        url = reverse('get_participants_per_profile')  
        response = self.client.get(url)


        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
       
        response_data = response.json()
        self.assertIn('1', response_data)  
        self.assertIn('job_profile_id', response_data['1']) 
        self.assertIn('number_of_participants', response_data['1'])

        self.assertEqual(response_data['1']['job_profile_id'], self.job_profile.id)
        self.assertEqual(response_data['1']['number_of_participants'], 1) 

from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from trainings.models import  Training
from unittest.mock import patch, MagicMock
import json

class GenerateManagementReportTestCase(APITestCase):

    def setUp(self):
        """
        Set up test data and client
        """
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass")
        
        self.campagne = Campagne.objects.create(
            created_by=self.user, 
            security_display_threshold=5, 
            aggregate_over_single_profiles=False,
            one_token_mode=True,
        )
        self.invitation = Invitation.objects.create(
            token='f5022aa4-39a6-4921-a691-a14384cfcc9f',
            created_by=self.user,
            reusable=True
        )
        self.threat_event = ThreatEvent.objects.create(
            event_name="Phishing", 
            event_description="A phishing threat event"
        )
        self.threat_area = ThreatArea.objects.create(
            area_name="Mailsystem", 
            area_description="A Mailsystem"
        )
        self.threat_vector = ThreatVector.objects.create(
            threat_event=self.threat_event, 
            threat_area=self.threat_area,
            threat_vector_description="Phishing over Mailsystem"
        )
        

        self.job_profile1 = JobProfile.objects.create(job_name="Backoffice Employee", job_description="A standard profile for sales activities", job_tasks="External sales to customers")
        self.job_profile2 = JobProfile.objects.create(job_name="Field Employee", job_description="A standard profile for office activities", job_tasks="")

        self.competence_test1 = CompetenceTest.objects.create(job_profile=self.job_profile1)
        self.competence_test2 = CompetenceTest.objects.create(job_profile=self.job_profile2)

        self.competence_dimension1 = CompetenceDimension.objects.create(dimension_name="Threat Awareness")
        self.competence_dimension2 = CompetenceDimension.objects.create(dimension_name="Threat Identification")

        self.competence_test_result1 = CompetenceTestResult.objects.create(job_profile=self.job_profile1, created_by=self.user)
        self.competence_test_result2 = CompetenceTestResult.objects.create(job_profile=self.job_profile2, created_by=self.user)

        self.training1 = Training.objects.create(training_name="Social Engineering Training")
        self.training2 = Training.objects.create(training_name="Phishing Training")
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation",
            threat_vector=self.threat_vector,
            job_profile=self.job_profile1
        )

    @patch('campagne.views.get_invitations')
    @patch('campagne.views.get_participants_per_profile')
    @patch('campagne.views.get_competence_test_results')
    @patch('campagne.views.generate_threat_chart')
    @patch('campagne.views.generate_competence_bar_chart')
    @patch('campagne.views.generate_job_profile_distribution')
    @patch('campagne.views.render_to_string')
    def test_generate_management_report(self, mock_render_to_string, mock_generate_job_profile_distribution, mock_generate_competence_bar_chart, mock_generate_threat_chart, mock_get_competence_test_results, mock_get_participants_per_profile, mock_get_invitations):
        """
        Test the generation of the management report, ensuring it returns a PDF.
        """
        mock_invitations = MagicMock()
        mock_invitations.data = [
            {
                "email_encrypted": "encryptedemail1@example.com",
                "is_participated": False,
                "created_by": self.user.id,
                "reusable": True,
                "usage_active": True,
                "tokenCounter": 0,
                "token": "f5022aa4-39a6-4921-a691-a14384cfcc9f"
            }
        ]
        mock_get_invitations.return_value = mock_invitations
        mock_job_profiles = MagicMock()
        mock_job_profiles.data = {
            '0': {'job_profile_id': 0, 'number_of_participants': 5, 'job_profile_name': 'Alle', 'job_profile_description': 'Develops software', 'job_profile_tasks': 'Coding', 'number_of_threat_situations': 1},
        }
        mock_get_participants_per_profile.return_value = mock_job_profiles
        mock_competence_test_results = MagicMock()
        mock_competence_test_results.data = {
            "0": {
                "total_threat_situation_scores": {"total_scoredPoints": 75},
                "number_of_threats": 9,
                "total_competence_dimension_scores": {
                    "1": {"total_scoredPoints": 14, "description": "Threat Awareness"},
                    "2": {"total_scoredPoints": 10, "description": "Threat Identification"},
                    "3": {"total_scoredPoints": 9, "description": "Threat Impact Assessment"},
                    "4": {"total_scoredPoints": 13, "description": "Tactic Choice"},
                    "5": {"total_scoredPoints": 9, "description": "Tactic Justification"},
                    "6": {"total_scoredPoints": 11, "description": "Tactic Mastery"},
                    "7": {"total_scoredPoints": 16, "description": "Tactic Check & Follow-Up"}
                },
                "profile_name": "Alle",
                "number_of_participants": 5
            }
        }
        mock_get_competence_test_results.return_value = mock_competence_test_results
        mock_generate_threat_chart.return_value = 'mocked_threat_chart'
        mock_generate_competence_bar_chart.return_value = 'mocked_competence_bar_chart'
        mock_generate_job_profile_distribution.return_value = 'mocked_distribution'
        mock_render_to_string.return_value = '<html><body>Management Report</body></html>'

        url = reverse('generate_management_report')  
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn('attachment; filename="management_report.pdf"', response['Content-Disposition'])

        mock_get_invitations.assert_called_once()
        mock_get_participants_per_profile.assert_called_once()
        mock_get_competence_test_results.assert_called()
        mock_generate_threat_chart.assert_called()
        mock_generate_competence_bar_chart.assert_called()
        mock_render_to_string.assert_called_once()

