from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import *
import os
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from datetime import datetime
from threats.models import ThreatArea, ThreatEvent, ThreatVector, ThreatSituation
import json
from django.test import RequestFactory
from django.http import JsonResponse
from .views import generate_individual_report  
from unittest.mock import patch

class CompetenceDimensionViewSetTests(APITestCase):
    
    def setUp(self):
        self.competence_dimension = CompetenceDimension.objects.create(
            dimension_name="Threat Awareness",
            dimension_description="The Threat Awareness description"
        )
        self.url = reverse('competencedimension-list')

    def test_list_competence_dimensions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) 

    def test_create_competence_dimension(self):
        data = {
            'dimension_name': 'Threat Identification',
            'dimension_description': 'Competence in identifying security threats'
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CompetenceDimension.objects.count(), 2)

    def test_retrieve_competence_dimension(self):
        response = self.client.get(reverse('competencedimension-detail', args=[self.competence_dimension.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['dimension_name'], 'Threat Awareness')

    def test_update_competence_dimension(self):
        data = {
            'dimension_name': 'Threat Awareness',
            'dimension_description': 'Updated Threat Awareness description'
        }
        response = self.client.put(reverse('competencedimension-detail', args=[self.competence_dimension.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.competence_dimension.refresh_from_db()
        self.assertEqual(self.competence_dimension.dimension_name, 'Threat Awareness')

    def test_delete_competence_dimension(self):
        response = self.client.delete(reverse('competencedimension-detail', args=[self.competence_dimension.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CompetenceDimension.objects.count(), 0)


class CompetenceTestViewSetTests(APITestCase):
    
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
            job_name="Innendienst", 
            job_description="A standard profile for office activities"
        )
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="2.1", 
            threat_description="A standard profile for office activities",
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )
        self.competence_test = CompetenceTest.objects.create(job_profile=self.job_profile)

        self.competence_test.threat_situations.set([self.threat_situation])
        self.url = reverse('competencetest-list')

    def test_list_competence_tests(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_competence_test(self):
        new_job_profile = JobProfile.objects.create(
            job_name="New Job Profile",
            job_description="New job profile description"
        )
        new_competence_test = CompetenceTest.objects.create(job_profile=new_job_profile)
        new_competence_test.threat_situations.set([self.threat_situation])

        new_competence_test.save()
        
        self.assertEqual(CompetenceTest.objects.count(), 2)
        
        
    def test_retrieve_competence_test(self):
        response = self.client.get(reverse('competencetest-detail', args=[self.competence_test.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_competence_test(self):
        updated_job_profile = JobProfile.objects.create(
            job_name="Updated Job Profile",
            job_description="New job profile description"
        )

        self.competence_test.job_profile = updated_job_profile
        self.competence_test.save()
       
        updated_competence_test = CompetenceTest.objects.get(id=self.competence_test.id)
        self.assertEqual(updated_competence_test.job_profile, updated_job_profile)

    def test_delete_competence_test(self):
        response = self.client.delete(reverse('competencetest-detail', args=[self.competence_test.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CompetenceTest.objects.count(), 0)

    def test_filter_by_job_profile(self):
        url = f"{self.url}?job_profile={self.job_profile.id}"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class QuestionItemViewSetTests(APITestCase):

    def setUp(self):
        self.competence_dimension = CompetenceDimension.objects.create(
            dimension_name="Threat Awareness",
            dimension_description="The Threat Awareness description"
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

        self.job_profile = JobProfile.objects.create(
            job_name="Innendienst", 
            job_description="A standard profile for office activities"
        )
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="2.1", 
            threat_description="A standard profile for office activities",
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )
        self.question_item = QuestionItem.objects.create(
            threat_situation=self.threat_situation,
            competence_dimension=self.competence_dimension,
            question="Which of the following possible queries do you think is most likely to be an attack?",
            question_name= '4.1',
            type=1
        )
       

        self.url = reverse('questionitem-list')

    def test_list_questions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_question(self):
        data = {
            'threat_situation': self.threat_situation.id,
            'competence_dimension':self.competence_dimension.id,
            'question': 'Which of the following possible queries do you think is most likely to be an attack?',
            'question_name': '4.2',
            'type': 1
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(QuestionItem.objects.count(), 2)

    def test_retrieve_question(self):
        response = self.client.get(reverse('questionitem-detail', args=[self.question_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['question'], 'Which of the following possible queries do you think is most likely to be an attack?')

    def test_update_question(self):
        data = {
            'threat_situation': self.threat_situation.id,
            'competence_dimension':self.competence_dimension.id,
            'question': 'Updated Question',
            'question_name': '4.1',
            'type': 1
        }
        response = self.client.put(reverse('questionitem-detail', args=[self.question_item.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.question_item.refresh_from_db()
        self.assertEqual(self.question_item.question, 'Updated Question')

    def test_delete_question(self):
        response = self.client.delete(reverse('questionitem-detail', args=[self.question_item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(QuestionItem.objects.count(), 0)



class TestItemViewSetTests(APITestCase):

    def setUp(self):
        self.competence_dimension = CompetenceDimension.objects.create(
            dimension_name="Threat Awareness",
            dimension_description="The Threat Awareness description"
        )
        self.job_profile = JobProfile.objects.create(
            job_name="Innendienst", 
            job_description="A standard profile for office activities"
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
        self.impulse = Impulse.objects.create(
            impulse_name="1.2 Bild-Impulse", 
        )
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="2.1", 
            threat_description="A standard profile for office activities",
            threat_vector=self.threat_vector,
            job_profile=self.job_profile
        )
        self.question_item = QuestionItem.objects.create(
            threat_situation=self.threat_situation,
            competence_dimension=self.competence_dimension,
            question="Which of the following possible queries do you think is most likely to be an attack?",
            question_name= '4.1',
            type=1
        )
        self.test_item = CompetenceTestItem.objects.create(competence_dimension=self.competence_dimension, impulse_item=self.impulse, threat_situation=self.threat_situation)
        self.test_item.question_item.set([self.question_item])

        self.url = reverse('competencetestitem-list')

    def test_list_test_items(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_competence_test_item(self):
        competence_test_item = CompetenceTestItem.objects.create(
            threat_situation=self.threat_situation,
            competence_dimension=self.competence_dimension,
            impulse_item=self.impulse
        )
        
        competence_test_item.question_item.add(self.question_item)

        self.assertEqual(CompetenceTestItem.objects.count(), 2)
        self.assertEqual(competence_test_item.threat_situation, self.threat_situation)
        self.assertEqual(competence_test_item.competence_dimension, self.competence_dimension)
        self.assertEqual(competence_test_item.impulse_item, self.impulse)
        self.assertIn(self.question_item, competence_test_item.question_item.all())  

    def test_update_competence_test_item(self):
        competence_test_item = CompetenceTestItem.objects.create(
            threat_situation=self.threat_situation,
            competence_dimension=self.competence_dimension,
            impulse_item=self.impulse
        )
        
        new_competence_dimension = CompetenceDimension.objects.create(
            dimension_name="New Threat Awareness",
            dimension_description="New description"
        )
        competence_test_item.competence_dimension = new_competence_dimension
        competence_test_item.save()

        updated_item = CompetenceTestItem.objects.get(id=competence_test_item.id)
        
        self.assertEqual(updated_item.competence_dimension, new_competence_dimension)


    def test_retrieve_test_item(self):
        response = self.client.get(reverse('competencetestitem-detail', args=[self.test_item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_test_item(self):
        response = self.client.delete(reverse('competencetestitem-detail', args=[self.test_item.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_by_threat_situation(self):
        url = f"{self.url}?threat_situation={self.threat_situation.id}"
        response = self

class ImpulseModelTest(APITestCase):

    def setUp(self):
        self.impulse = Impulse.objects.create(
            impulse_name="Test Impulse"
        )
        self.url = reverse('impulse-list')


    def test_impulse_creation(self):
        self.assertEqual(self.impulse.impulse_name, "Test Impulse")
        self.assertIsInstance(self.impulse, Impulse)
    
    def test_impulse_str(self):
        self.assertEqual(str(self.impulse), "Test Impulse")
    
    def test_impulse_max_length(self):
        max_length = self.impulse._meta.get_field('impulse_name').max_length
        self.assertEqual(max_length, 140)

    def test_impulse_nullability(self):
        impulse_null = Impulse.objects.create(impulse_name=None)
        self.assertIsNone(impulse_null.impulse_name)

    def test_update_impulse_item(self):
        self.impulse.impulse_name = "Updated Impulse"
        self.impulse.save()

        updated_impulse = Impulse.objects.get(id=self.impulse.id)
        
        self.assertEqual(updated_impulse.impulse_name, "Updated Impulse")
      

    def test_delete_impulse_item(self):
        response = self.client.delete(reverse('impulse-detail', args=[self.impulse.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class ImageItemTest(APITestCase):
    
    def setUp(self):
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="2.1",
            threat_description="A test threat situation"
        )

        self.image_path = os.path.join(settings.BASE_DIR, 'competence_tests/static/competence_tests/css/images/report-cover.jpg')

        with open(self.image_path, 'rb') as image_file:
            self.image = SimpleUploadedFile(
                name='test_image.jpg', 
                content=image_file.read(),
                content_type='image/jpeg'
            )

        self.image_item = ImageItem.objects.create(
            threat_situation=self.threat_situation,
            image_name="Test Image",
            image_field=self.image,
            image_description="Test image description"
        )

    def test_create_image_item(self):
        with open(self.image_path, 'rb') as image_file:
            image_data = image_file.read()

        image_data = {
            'threat_situation': self.threat_situation.id,
            'image_name': 'New Image',
            'image_field': SimpleUploadedFile(
                name='new_image.jpg',
                content=image_data,
                content_type='image/jpeg'
            ),
            'image_description': 'A new test image'
        }

        response = self.client.post(reverse('imageitem-list'), data=image_data, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ImageItem.objects.count(), 2)
        self.assertEqual(ImageItem.objects.last().image_name, 'New Image')

    def test_read_image_item(self):
        response = self.client.get(reverse('imageitem-detail', args=[self.image_item.id]))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['image_name'], self.image_item.image_name)

    def test_update_image_item(self):
        with open(self.image_path, 'rb') as image_file:
            image_data = image_file.read()
        updated_data = {
            'threat_situation': self.threat_situation.id,
            'image_name': 'Updated Image',
            'image_field': SimpleUploadedFile(
                name='updated_image.jpg',
                content=image_data,
                content_type='image/jpeg'
            ),
            'image_description': 'Updated description'
        }

        response = self.client.put(reverse('imageitem-detail', args=[self.image_item.id]), data=updated_data, format='multipart')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.image_item.refresh_from_db()
        self.assertEqual(self.image_item.image_name, 'Updated Image')

    def test_delete_image_item(self):
        initial_count = ImageItem.objects.count()
        self.assertEqual(initial_count, 1)

        response = self.client.delete(reverse('imageitem-detail', args=[self.image_item.id]))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(ImageItem.objects.count(), 0)

class EmailItemTest(APITestCase):

    def setUp(self):
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation"
        )

        self.sender_image_path = os.path.join(settings.BASE_DIR, 'competence_tests/static/competence_tests/css/images/report-cover.jpg')
        self.signed_image_path = os.path.join(settings.BASE_DIR, 'competence_tests/static/competence_tests/css/images/report-cover.jpg')


        with open(self.sender_image_path, 'rb') as image_file:
            self.sender_image = SimpleUploadedFile(
                name='test_sender_image.jpg', 
                content=image_file.read(),
                content_type='image/jpeg'
            )
        with open(self.signed_image_path, 'rb') as signed_image_file:
            self.signed_image = SimpleUploadedFile(
                name='test_signed_image.jpg',
                content=signed_image_file.read(),
                content_type='image/jpeg'
            )
        self.email_item = EmailItem.objects.create(
            threat_situation=self.threat_situation,
            email_name="Test Email",
            email_sender="test@sender.com",
            email_recipient="test@recipient.com",
            email_regarding="Test Subject",
            email_teaser="This is a test teaser.",
            email_content="This is the test content of the email.",
            email_image_sender=self.sender_image,
            email_date=timezone.now().time(),
            email_is_signed_image=self.signed_image,
        )

    def test_create_email_item(self):
        with open(self.sender_image_path, 'rb') as image_file:
            image_data = image_file.read()
        with open(self.signed_image_path, 'rb') as image_file:
            signed_image_data = image_file.read()
        new_email_data = {
            'threat_situation': self.threat_situation.id,
            'email_name': 'New Email',
            'email_sender': 'new_sender@domain.com',
            'email_recipient': 'new_recipient@domain.com',
            'email_regarding': 'New Subject',
            'email_teaser': 'This is a new email teaser.',
            'email_content': 'This is the new email content.',
            'email_image_sender': SimpleUploadedFile(
                name='new_sender_image.jpg',
                content=image_data,
                content_type='image/jpeg'
            ),
            'email_date': timezone.now().time(),
            'email_is_signed_image': SimpleUploadedFile(
                name='new_signed_image.jpg',
                content=signed_image_data,
                content_type='image/jpeg'
            )
        }

        response = self.client.post(reverse('emailitem-list'), data=new_email_data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(EmailItem.objects.count(), 2)
        self.assertEqual(EmailItem.objects.last().email_name, 'New Email')

    def test_read_email_item(self):
        response = self.client.get(reverse('emailitem-detail', args=[self.email_item.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email_name'], self.email_item.email_name)

    def test_update_email_item(self):
        with open(self.sender_image_path, 'rb') as sender_image_file:
            sender_image_data = sender_image_file.read()
        with open(self.signed_image_path, 'rb') as signed_image_file:
            signed_image_data = signed_image_file.read()
        # Prepare new data for updating the existing EmailItem
        updated_email_data = {
            'threat_situation': self.threat_situation.id,
            'email_name': 'Updated Email Name',
            'email_sender': 'updated_sender@domain.com',
            'email_recipient': 'updated_recipient@domain.com',
            'email_regarding': 'Updated Subject',
            'email_teaser': 'Updated teaser.',
            'email_content': 'Updated email content.',
            'email_image_sender': SimpleUploadedFile(
                name='updated_sender_image.jpg',
                content=sender_image_data,
                content_type='image/jpeg'
            ),
            'email_date': timezone.now().time(),
            'email_is_signed_image': SimpleUploadedFile(
                name='updated_signed_image.jpg',
                content=signed_image_data,
                content_type='image/jpeg'
            )
        }

        response = self.client.put(
            reverse('emailitem-detail', args=[self.email_item.id]), 
            updated_email_data,
            format='multipart'  
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.email_item.refresh_from_db()
        self.assertEqual(self.email_item.email_name, 'Updated Email Name')


    def test_delete_email_item(self):
        initial_count = EmailItem.objects.count()
        self.assertEqual(initial_count, 1)

        response = self.client.delete(reverse('emailitem-detail', args=[self.email_item.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EmailItem.objects.count(), 0)



class EmailImpulseCRUDTest(APITestCase):

    def setUp(self):
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation"
        )

        self.email_item1 = EmailItem.objects.create(
            threat_situation=self.threat_situation,
            impulse_number="1.2",
            email_name="Test Email 1",
            email_sender="test1@sender.com",
            email_recipient="test1@recipient.com",
            email_regarding="Test Subject 1",
            email_teaser="This is a test teaser 1.",
            email_content="This is the test content of the email 1.",
            email_date=timezone.now().time()
        )

        self.email_item2 = EmailItem.objects.create(
            threat_situation=self.threat_situation,
            impulse_number="1.2",
            email_name="Test Email 2",
            email_sender="test2@sender.com",
            email_recipient="test2@recipient.com",
            email_regarding="Test Subject 2",
            email_teaser="This is a test teaser 2.",
            email_content="This is the test content of the email 2.",
            email_date=timezone.now().time()
        )

        self.email_impulse = EmailImpulse.objects.create(
            impulse_text="This is the initial impulse text.",
        )
        self.email_impulse.email.set([self.email_item1, self.email_item2])

    def test_create_email_impulse(self):
        
        new_email_impulse_data = EmailImpulse.objects.create(
            impulse_text="This is a new impulse text.",
        )

        new_email_impulse_data.email.set([self.email_item1, self.email_item2])  
        new_email_impulse_data.save()



        self.assertEqual(EmailImpulse.objects.count(), 2) 

        created_email_impulse = EmailImpulse.objects.last()
        self.assertEqual(created_email_impulse.impulse_text, 'This is a new impulse text.')
        self.assertEqual(created_email_impulse.email.count(), 2)

    def test_read_email_impulse(self):
        response = self.client.get(reverse('impulse-detail', args=[self.email_impulse.id]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['impulse_text'], self.email_impulse.impulse_text)
        self.assertEqual(len(response.data['email']), 2) 

    def test_update_email_impulse(self):
       
        self.email_impulse.impulse_text = "Updated impulse text"
        self.email_impulse.email.set([self.email_item1, self.email_item2]) 
        self.email_impulse.save()

        updated_email_impulse = EmailImpulse.objects.get(id=self.email_impulse.id)
        self.assertEqual(updated_email_impulse.impulse_text, "Updated impulse text")
        self.assertEqual(updated_email_impulse.email.count(), 2)


    def test_delete_email_impulse(self):
        self.assertEqual(EmailImpulse.objects.count(), 1)

        response = self.client.delete(reverse('impulse-detail', args=[self.email_impulse.id]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(EmailImpulse.objects.count(), 0)  


class ChoiceItemModelTest(APITestCase):
    
    def setUp(self):
        self.question = QuestionItem.objects.create(
            question_name="4.1",
            question="Which of the following possible queries do you think is most likely to be an attack?",
        )
        self.choice_item = ChoiceItem.objects.create(
            question=self.question,
            option="Scenario 1",
            answer_rating=2
        )

    def test_create_choice_item(self):
        choice1 = ChoiceItem.objects.create(
            question=self.question,
            option="Scenario 1",
            answer_rating=2
        )
        self.assertEqual(choice1.option, "Scenario 1")
        self.assertEqual(choice1.answer_rating, 2)
        self.assertEqual(choice1.question, self.question)
    
    def test_default_answer_rating(self):
        choice = ChoiceItem.objects.create(
            question=self.question,
            option="Scenario 1"
        )
        self.assertEqual(choice.answer_rating, 0)

    def test_update_choice_item(self):
        self.choice_item.option = "Scenario 1"
        self.choice_item.answer_rating = 0
        self.choice_item.save()
        
        updated_choice = ChoiceItem.objects.get(id=self.choice_item.id)
        self.assertEqual(updated_choice.option, "Scenario 1")
        self.assertEqual(updated_choice.answer_rating, 0)

    def test_delete_choice_item(self):
        self.choice_item.delete()
        self.assertEqual(ChoiceItem.objects.count(), 0) 

    def test_choice_item_str(self):
        choice = ChoiceItem.objects.create(
            question=self.question,
            option="Scneario 2",
            answer_rating=1
        )
        self.assertEqual(str(choice), self.question.question_name)

    

class ChatInterfaceModelCRUDTest(APITestCase):

    def setUp(self):
        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation"
        )
        self.sample_image = os.path.join(settings.BASE_DIR, 'competence_tests/static/competence_tests/css/images/report-cover.jpg')


        with open(self.sample_image, 'rb') as image_file:
            self.sample_image = SimpleUploadedFile(
                name='test_sample_image.jpg', 
                content=image_file.read(),
                content_type='image/jpeg'
            )

        self.chat_interface = ChatInterface.objects.create(
            threat_situation=self.threat_situation,
            impulse_number="1",
            chat_sender_name="John Doe",
            chat_sender_known=True,
            chat_sender_image=self.sample_image,
            chat_message_incoming="Hello!",
            chat_message_incoming_date=datetime.now().time(),
            chat_message_outgoing="Hi, how can I help?",
            chat_message_outgoing_date=datetime.now().time(),
            chat_message_incoming_2="I need assistance.",
            chat_message_incoming_date_2=datetime.today()
        )

    def test_create_chat_interface(self):
        chat = ChatInterface.objects.create(
            threat_situation=self.threat_situation,
            impulse_number="1",
            chat_sender_name="Jane Smith",
            chat_sender_known=False,
            chat_message_incoming="Need help",
            chat_message_incoming_date=datetime.now().time(),
            chat_message_outgoing="What can I do for you?",
            chat_message_outgoing_date=datetime.now().time()
        )
        self.assertEqual(ChatInterface.objects.count(), 2)  
        self.assertEqual(chat.chat_sender_name, "Jane Smith")
        self.assertFalse(chat.chat_sender_known)
        self.assertEqual(chat.impulse_number, "1")

    def test_read_chat_interface(self):
        chat = ChatInterface.objects.get(id=self.chat_interface.id)
        self.assertEqual(chat.chat_sender_name, "John Doe")
        self.assertEqual(chat.chat_message_incoming, "Hello!")
    
    def test_update_chat_interface(self):
        self.chat_interface.chat_message_outgoing = "How may I assist you?"
        self.chat_interface.save()

        updated_chat = ChatInterface.objects.get(id=self.chat_interface.id)
        self.assertEqual(updated_chat.chat_message_outgoing, "How may I assist you?")
    
    def test_delete_chat_interface(self):
        self.chat_interface.delete()
        
        self.assertEqual(ChatInterface.objects.count(), 0) 


class ChatImpulseModelCRUDTest(APITestCase):

    def setUp(self):

        self.threat_situation = ThreatSituation.objects.create(
            threat_situation_identificator="1.2",
            threat_description="A test threat situation"
        )
        self.chat_interface1 = ChatInterface.objects.create(
            threat_situation=self.threat_situation,
            impulse_number="1",
            chat_sender_name="John Doe",
            chat_sender_known=True,
            chat_message_incoming="Hello!",
            chat_message_incoming_date=datetime.now().time(),
            chat_message_outgoing="Hi, how can I help?",
            chat_message_outgoing_date=datetime.now().time()
        )
        
        self.chat_interface2 = ChatInterface.objects.create(
            threat_situation=self.threat_situation,
            impulse_number="1",
            chat_sender_name="Jane Smith",
            chat_sender_known=False,
            chat_message_incoming="Need help",
            chat_message_incoming_date=datetime.now().time(),
            chat_message_outgoing="Sure, I can assist.",
            chat_message_outgoing_date=datetime.now().time()
        )

        self.chat_impulse = ChatImpulse.objects.create(
            impulse_text="This is an impulse related to a chat."
        )
        self.chat_impulse.chat_interface.set([self.chat_interface1, self.chat_interface2])

    def test_create_chat_impulse(self):
        chat_impulse = ChatImpulse.objects.create(
            impulse_text="New impulse text"
        )
        chat_impulse.chat_interface.set([self.chat_interface1])  
        chat_impulse.save()

        self.assertEqual(ChatImpulse.objects.count(), 2) 
        self.assertEqual(chat_impulse.impulse_text, "New impulse text")
        self.assertEqual(chat_impulse.chat_interface.count(), 1)

    def test_read_chat_impulse(self):
        chat_impulse = ChatImpulse.objects.get(id=self.chat_impulse.id)
        self.assertEqual(chat_impulse.impulse_text, "This is an impulse related to a chat.")
        self.assertEqual(chat_impulse.chat_interface.count(), 2)

    def test_update_chat_impulse(self):
        self.chat_impulse.impulse_text = "Updated impulse text"
        self.chat_impulse.chat_interface.set([self.chat_interface2])  
        self.chat_impulse.save()

        updated_chat_impulse = ChatImpulse.objects.get(id=self.chat_impulse.id)
        self.assertEqual(updated_chat_impulse.impulse_text, "Updated impulse text")
        self.assertEqual(updated_chat_impulse.chat_interface.count(), 1)

    def test_delete_chat_impulse(self):
        self.chat_impulse.delete()

        self.assertEqual(ChatImpulse.objects.count(), 0)  
        self.assertEqual(ChatInterface.objects.count(), 2) 



class GenerateIndividualReportTest(APITestCase):

    def setUp(self):
        self.job_profile = JobProfile.objects.create(job_name="Backoffice Employee")
        self.competence_dimension = CompetenceDimension.objects.create(dimension_name="Threat Awareness")

        self.factory = RequestFactory()

        self.valid_data = {
            "competenceDimensionScore": [2, 1,1],
            "totalPointsScored": 25,
            "test_situations": [
                {
                    "threat_vector": {
                        "threatVectorText": "Phishing Attack",
                        "threat_vector_description": "Email-based phishing attack",
                        "test_items": [
                            {
                                "competence_dimension": {"dimension_name": "Problem Solving"},
                                "question_item": [{"points": 1}]
                            }
                        ]
                    },
                    "pointsScored": 12
                }
            ],
            "job_profile_id": self.job_profile.id
        }

    @patch('competence_tests.views.generate_competence_bar_chart_per_threat')
    @patch('competence_tests.views.generate_threat_chart')
    @patch('competence_tests.views.generate_competence_bar_chart')
    @patch('competence_tests.views.HTML') 
    def test_generate_individual_report_success(self, mock_html, mock_generate_competence_bar_chart, mock_generate_threat_chart, mock_generate_competence_bar_chart_per_threat):
        mock_generate_competence_bar_chart_per_threat.return_value = "Mocked Bar Chart Per Threat"
        mock_generate_threat_chart.return_value = "Mocked Threat Chart"
        mock_generate_competence_bar_chart.return_value = "Mocked Competence Bar Chart"
        mock_html_instance = mock_html.return_value
        mock_html_instance.write_pdf.return_value = b""

        request = self.factory.post('/generate_individual_report/', data=json.dumps(self.valid_data), content_type='application/json')

        response = generate_individual_report(request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')
        self.assertIn(b"", response.content)

    def test_generate_individual_report_invalid_json(self):
        request = self.factory.post('/generate_individual_report/', data="Invalid JSON", content_type='application/json')

        response = generate_individual_report(request)

        self.assertEqual(response.status_code, 400)
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid JSON'})

    def test_generate_individual_report_missing_job_profile(self):
        invalid_data = self.valid_data.copy()
        invalid_data['job_profile_id'] = 999  

        request = self.factory.post('/generate_individual_report/', data=json.dumps(invalid_data), content_type='application/json')

        with self.assertRaises(JobProfile.DoesNotExist):
            generate_individual_report(request)
