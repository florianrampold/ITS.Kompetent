from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import (
    TargetAudience, DeliveryMethod, Language, TrainingGroup, Training,
    TrainingCategory, ThreatEvent
)
from competence_tests.models import CompetenceDimension


class TrainingModelTests(APITestCase):

    def setUp(self):
        self.target_audience = TargetAudience.objects.create(audience_name="Developers")
        self.delivery_method = DeliveryMethod.objects.create(delivery_method="Online")
        self.language = Language.objects.create(language="English")
        self.training_group = TrainingGroup.objects.create(identifier="Group 1")
        self.threat_event = ThreatEvent.objects.create(event_name="Phishing Attack", event_description="Email phishing attack")

        self.competence_dimension = CompetenceDimension.objects.create(
            dimension_name="Threat Awareness",
            dimension_description="Threat Awareness Description"
        )

        self.training = Training.objects.create(
            training_group=self.training_group,
            training_provider="Provider A",
            training_name="Security Awareness Training",
            costs=1,  
            certification=1,  
            training_url="https://example.com/training"
        )
        self.training.delivery_method.add(self.delivery_method)
        self.training.language.add(self.language)
        self.training.competence_dimensions.add(self.competence_dimension)
        self.training.threat_event.add(self.threat_event)

        self.training_category = TrainingCategory.objects.create(
            training_category_name="Cybersecurity Basics",
            training_category_description="Introduction to Cybersecurity"
        )
        self.training_category.threat_event.add(self.threat_event)

    def test_list_trainings(self):
        url = reverse('training-list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['training_name'], 'Security Awareness Training')

    def test_create_training(self):
        url = reverse('training-list')
        data = {
            'training_group': self.training_group.id,
            'training_provider': 'Provider B',
            'training_name': 'Advanced Security Training',
            'costs': 2,  
            'certification': 2,  
            'training_url': 'https://example.com/advanced_training',
            'delivery_method': [self.delivery_method.id],
            'language': [self.language.id],
            'competence_dimensions': [self.competence_dimension.id],
            'threat_event': [self.threat_event.id]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Training.objects.count(), 2)

    def test_update_training(self):
        url = reverse('training-detail', args=[self.training.id])
        data = {
            'training_group': self.training_group.id,
            'training_provider': 'Updated Provider',
            'training_name': 'Updated Security Awareness Training',
            'costs': 3,  #
            'certification': 1,
            'training_url': 'https://example.com/updated_training',
            'delivery_method': [self.delivery_method.id],
            'language': [self.language.id],
            'competence_dimensions': [self.competence_dimension.id],
            'threat_event': [self.threat_event.id]
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.training.refresh_from_db()
        self.assertEqual(self.training.training_provider, 'Updated Provider')

    def test_delete_training(self):
        url = reverse('training-detail', args=[self.training.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Training.objects.count(), 0)


class TrainingCategoryTests(APITestCase):

    def setUp(self):
        self.threat_event = ThreatEvent.objects.create(event_name="Phishing Attack", event_description="Email phishing attack")
        self.training_category = TrainingCategory.objects.create(
            training_category_name="Cybersecurity Basics",
            training_category_description="Introduction to Cybersecurity"
        )
        self.training_category.threat_event.add(self.threat_event)

    def test_list_training_categories(self):
        url = reverse('trainingcategory-list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['training_category_name'], 'Cybersecurity Basics')

    def test_create_training_category(self):
        url = reverse('trainingcategory-list')
        data = {
            'training_category_name': 'Advanced Cybersecurity',
            'training_category_description': 'In-depth look at cybersecurity',
            'threat_event': [self.threat_event.id]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TrainingCategory.objects.count(), 2)

    def test_update_training_category(self):
        url = reverse('trainingcategory-detail', args=[self.training_category.id])
        data = {
            'training_category_name': 'Updated Cybersecurity Basics',
            'training_category_description': 'Updated introduction to cybersecurity',
            'threat_event': [self.threat_event.id]
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.training_category.refresh_from_db()
        self.assertEqual(self.training_category.training_category_name, 'Updated Cybersecurity Basics')

    def test_delete_training_category(self):
        url = reverse('trainingcategory-detail', args=[self.training_category.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TrainingCategory.objects.count(), 0)

