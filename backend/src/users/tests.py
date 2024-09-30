from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserProfile

class UserProfileTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass123'
        )

    def test_create_user_profile(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=True
        )

        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(user_profile.user, self.user)
        self.assertTrue(user_profile.is_campagne_manager)

    def test_default_is_campagne_manager(self):
        user_profile = UserProfile.objects.create(
            user=self.user
        )

        self.assertFalse(user_profile.is_campagne_manager)

    def test_user_profile_str_method(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=False
        )

        self.assertEqual(str(user_profile), self.user.username)

    def test_one_to_one_relationship(self):
        user_profile = UserProfile.objects.create(
            user=self.user
        )

        with self.assertRaises(Exception):
            UserProfile.objects.create(
                user=self.user
            )

    def test_update_user_profile(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=False
        )

        user_profile.is_campagne_manager = True
        user_profile.save()

        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertTrue(updated_profile.is_campagne_manager)



class ObtainJWTTokenWithCookieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='campagne_manager', password='password123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=True
        )

        self.non_manager_user = get_user_model().objects.create_user(
            username='non_manager', password='password123'
        )
        self.non_manager_profile = UserProfile.objects.create(
            user=self.non_manager_user,
            is_campagne_manager=False
        )

        self.url = reverse('obtain_jwt_token_with_cookie')

        self.client = APIClient()

    def test_valid_login_for_campagne_manager(self):
        data = {'username': 'campagne_manager', 'password': 'password123'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('accessToken', response.cookies)
        self.assertIn('refreshToken', response.cookies)

        self.assertEqual(response.data['user'], 'campagne_manager')
        self.assertEqual(response.data['message'], 'Authenticated successfully')

    def test_invalid_credentials(self):
        data = {'username': 'campagne_manager', 'password': 'wrongpassword'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'error': 'Invalid credentials.'})

    def test_non_campagne_manager_login(self):
        data = {'username': 'non_manager', 'password': 'password123'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'error': 'Only Campagne Managers can log in.'})

    def test_invalid_login_empty_fields(self):
        data = {'username': '', 'password': ''}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'error': 'Invalid credentials.'})


from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import UserProfile

class UserProfileTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpass123'
        )

    def test_create_user_profile(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=True
        )

        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(user_profile.user, self.user)
        self.assertTrue(user_profile.is_campagne_manager)

    def test_default_is_campagne_manager(self):
        user_profile = UserProfile.objects.create(
            user=self.user
        )

        self.assertFalse(user_profile.is_campagne_manager)

    def test_user_profile_str_method(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=False
        )

        self.assertEqual(str(user_profile), self.user.username)

    def test_one_to_one_relationship(self):
        user_profile = UserProfile.objects.create(
            user=self.user
        )

        with self.assertRaises(Exception):
            UserProfile.objects.create(
                user=self.user
            )

    def test_update_user_profile(self):
        user_profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=False
        )

        user_profile.is_campagne_manager = True
        user_profile.save()

        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertTrue(updated_profile.is_campagne_manager)



class ObtainJWTTokenWithCookieTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='campagne_manager', password='password123'
        )
        self.profile = UserProfile.objects.create(
            user=self.user,
            is_campagne_manager=True
        )

        self.non_manager_user = get_user_model().objects.create_user(
            username='non_manager', password='password123'
        )
        self.non_manager_profile = UserProfile.objects.create(
            user=self.non_manager_user,
            is_campagne_manager=False
        )

        self.url = reverse('obtain_jwt_token_with_cookie')

        self.client = APIClient()

    def test_valid_login_for_campagne_manager(self):
        data = {'username': 'campagne_manager', 'password': 'password123'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('accessToken', response.cookies)
        self.assertIn('refreshToken', response.cookies)

        self.assertEqual(response.data['user'], 'campagne_manager')
        self.assertEqual(response.data['message'], 'Authenticated successfully')

    def test_invalid_credentials(self):
        data = {'username': 'campagne_manager', 'password': 'wrongpassword'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'error': 'Invalid credentials.'})

    def test_non_campagne_manager_login(self):
        data = {'username': 'non_manager', 'password': 'password123'}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.json(), {'error': 'Only Campagne Managers can log in.'})

    def test_invalid_login_empty_fields(self):
        data = {'username': '', 'password': ''}
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'error': 'Invalid credentials.'})


