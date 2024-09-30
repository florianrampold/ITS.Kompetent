from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import ThreatSituation, ThreatVector, ThreatEvent, ThreatArea, JobProfile
from .serializers import ThreatAreaSerializer, ThreatEventSerializer, ThreatVectorSerializer


class ThreatAreaViewSetTests(APITestCase):
    def setUp(self):
        self.threat_area = ThreatArea.objects.create(area_name="Test Threat Area")
        self.url = reverse('threatarea-list')

    def test_list_threat_areas(self):
        response = self.client.get(self.url)
        threat_areas = ThreatArea.objects.all()
        serializer = ThreatAreaSerializer(threat_areas, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_threat_area(self):
        data = {'area_name': 'New Threat Area'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ThreatArea.objects.count(), 2)
        self.assertEqual(ThreatArea.objects.get(id=response.data['id']).area_name, 'New Threat Area')

    def test_retrieve_threat_area(self):
        response = self.client.get(reverse('threatarea-detail', args=[self.threat_area.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['area_name'], self.threat_area.area_name)

    def test_update_threat_area(self):
        data = {'area_name': 'Updated Threat Area'}
        response = self.client.put(reverse('threatarea-detail', args=[self.threat_area.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.threat_area.refresh_from_db()
        self.assertEqual(self.threat_area.area_name, 'Updated Threat Area')

    def test_delete_threat_area(self):
        response = self.client.delete(reverse('threatarea-detail', args=[self.threat_area.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ThreatArea.objects.count(), 0)


class ThreatEventViewSetTests(APITestCase):
    def setUp(self):
        self.threat_event = ThreatEvent.objects.create(event_name="Test Threat Event")
        self.url = reverse('threatevent-list')

    def test_list_threat_events(self):
        response = self.client.get(self.url)
        threat_events = ThreatEvent.objects.all()
        serializer = ThreatEventSerializer(threat_events, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_threat_event(self):
        data = {'event_name': 'New Threat Event'}
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ThreatEvent.objects.count(), 2)
        self.assertEqual(ThreatEvent.objects.get(id=response.data['id']).event_name, 'New Threat Event')

    def test_retrieve_threat_event(self):
        response = self.client.get(reverse('threatevent-detail', args=[self.threat_event.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['event_name'], self.threat_event.event_name)

    def test_update_threat_event(self):
        data = {'event_name': 'Updated Threat Event'}
        response = self.client.put(reverse('threatevent-detail', args=[self.threat_event.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.threat_event.refresh_from_db()
        self.assertEqual(self.threat_event.event_name, 'Updated Threat Event')

    def test_delete_threat_event(self):
        response = self.client.delete(reverse('threatevent-detail', args=[self.threat_event.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ThreatEvent.objects.count(), 0)


class ThreatVectorViewSetTests(APITestCase):
    def setUp(self):
        # Create instances of ThreatEvent and ThreatArea for the ForeignKey fields
        self.threat_event = ThreatEvent.objects.create(
            event_name="Phishing", 
            event_description="A phishing threat event"
        )
        self.threat_area = ThreatArea.objects.create(
            area_name="Mailsystem", 
            area_description="A mailsystem"
        )
        self.threat_vector = ThreatVector.objects.create(
            threat_event=self.threat_event,
            threat_area=self.threat_area,
            threat_vector_description="Phishing over Mailsystem"
        )
        
        self.url = reverse('threatvector-list')

    def test_list_threat_vectors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  
    
    def test_create_threat_vector(self):
        new_threat_vector = ThreatVector.objects.create(
            threat_event=self.threat_event,
            threat_area=self.threat_area,
            threat_vector_description="Phishing over Instant-Messenger"
        )
        new_threat_vector.save()
       
        self.assertEqual(ThreatVector.objects.count(), 2) 
        self.assertEqual(ThreatVector.objects.last().threat_vector_description, 'Phishing over Instant-Messenger')

    def test_retrieve_threat_vector(self):
        response = self.client.get(reverse('threatvector-detail', args=[self.threat_vector.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['threat_vector_description'], self.threat_vector.threat_vector_description)

    def test_update_threat_vector(self):
        self.threat_vector.threat_vector_description = "Malware attack in cybersecurity"
        self.threat_vector.save()

        updated_threat_vector = ThreatVector.objects.get(id=self.threat_vector.id)
        self.assertEqual(updated_threat_vector.threat_vector_description, 'Malware attack in cybersecurity')

    def test_delete_threat_vector(self):
        response = self.client.delete(reverse('threatvector-detail', args=[self.threat_vector.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ThreatVector.objects.count(), 0)


class ThreatSituationViewSetTests(APITestCase):

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

        self.job_profile = JobProfile.objects.create(
            job_name="Backoffice Employee", 
            job_description="A standard profile for office activities"
        )

        self.url = reverse('threatsituation-list')

    def test_list_threat_situations(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  

    def test_create_threat_situation(self):
        data = {
            'threat_situation_identificator': '1.1',
            'threat_description': 'A detailed description of the threat situation.',
            'threat_vector': self.threat_vector.id,  
            'job_profile': self.job_profile.id      
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ThreatSituation.objects.count(), 1) 

        threat_situation = ThreatSituation.objects.first()
        self.assertEqual(threat_situation.threat_situation_identificator, '1.1')
        self.assertEqual(threat_situation.threat_description, 'A detailed description of the threat situation.')
        self.assertEqual(threat_situation.threat_vector, self.threat_vector)
        self.assertEqual(threat_situation.job_profile, self.job_profile)

    def test_retrieve_threat_situation(self):
        threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator='1.2',
            threat_description='Another description',
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )

        response = self.client.get(reverse('threatsituation-detail', args=[threat_situation.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['threat_situation_identificator'], '1.2')

    def test_update_threat_situation(self):
        threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator='1.3',
            threat_description='Description to be updated',
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )

        data = {
            'threat_situation_identificator': '1.3',
            'threat_description': 'Updated description',
            'threat_vector': self.threat_vector.id,
            'job_profile': self.job_profile.id
        }
        response = self.client.put(reverse('threatsituation-detail', args=[threat_situation.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        threat_situation.refresh_from_db()
        self.assertEqual(threat_situation.threat_situation_identificator, '1.3')
        self.assertEqual(threat_situation.threat_description, 'Updated description')

    def test_delete_threat_situation(self):
        threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator='1.4',
            threat_description='Description for deletion',
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )

        response = self.client.delete(reverse('threatsituation-detail', args=[threat_situation.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ThreatSituation.objects.count(), 0) 
