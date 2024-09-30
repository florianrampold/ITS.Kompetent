from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import JobProfile
from threats.models import ThreatEvent, ThreatArea, ThreatVector, ThreatSituation
from trainings.models import TrainingCategory


class JobProfileViewSetTests(APITestCase):

    def setUp(self):
        # Set up a JobProfile instance
        self.job_profile = JobProfile.objects.create(
            job_name="Field Employee",
            job_description="Responsible for sales",
            job_tasks="External sales to customers",
            show_job_profile=True
        )
        self.url = reverse('jobprofile-list')  

    def test_list_job_profiles(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

    def test_create_job_profile(self):
        data = {
            'job_name': 'Field Employee',
            'job_description': 'Responsible for sales',
            'job_tasks': 'External sales to customers',
            'show_job_profile': True
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobProfile.objects.count(), 2)  

    def test_retrieve_job_profile(self):
        response = self.client.get(reverse('jobprofile-detail', args=[self.job_profile.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['job_name'], 'Field Employee')

    def test_update_job_profile(self):
        data = {
            'job_name': 'Backoffice Employee',
            'job_description': 'Administration in backoffice',
            'job_tasks': 'Workin with mailsystem, collaboration tools..',
            'show_job_profile': True
        }
        response = self.client.put(reverse('jobprofile-detail', args=[self.job_profile.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.job_profile.refresh_from_db()
        self.assertEqual(self.job_profile.job_name, 'Backoffice Employee')

    def test_delete_job_profile(self):
        response = self.client.delete(reverse('jobprofile-detail', args=[self.job_profile.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(JobProfile.objects.count(), 0) 


class ThreatEventsByJobProfilesTests(APITestCase):

    def setUp(self):
        self.job_profile = JobProfile.objects.create(
            job_name="Field Employee",
            job_description="Responsible for sales",
            job_tasks="External sales to customers",
            show_job_profile=True
        )
        
        self.threat_event = ThreatEvent.objects.create(
            event_name="Phishing",
            event_description="A phishing attack"
        )

        self.threat_area = ThreatArea.objects.create(
            area_name="Mailsystem",
            area_description="A Mailsystem"
        )

        self.threat_vector = ThreatVector.objects.create(
            threat_event=self.threat_event,
            threat_area=self.threat_area,
            threat_vector_description="A phishing vector description"
        )

        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.1",
            threat_description="A description of a typical phishing situation in the daily work of field employees ",
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )

        self.training_category = TrainingCategory.objects.create(
            training_category_name="Social Engineering",
            training_category_description="A definition of social engineering"
        )
        self.training_category.threat_event.add(self.threat_event)

    def test_threat_events_by_job_profiles(self):
        url = reverse('job_profiles_by_threat_category')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        job_profile_data = response.data[0]
        self.assertEqual(job_profile_data['job_profile_name'], 'Field Employee')
        self.assertEqual(len(job_profile_data['threat_events']), 1)

        threat_event_data = job_profile_data['threat_events'][0]
        self.assertEqual(threat_event_data['id'], self.threat_event.id)
        self.assertEqual(threat_event_data['threat_areas'][0]['area_name'], 'Mailsystem')
        self.assertEqual(len(threat_event_data['threat_categories']), 1)
        self.assertEqual(threat_event_data['threat_categories'][0]['category_name'], 'Social Engineering')
