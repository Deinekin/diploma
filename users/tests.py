from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserAPITestCase(APITestCase):
    """User testcase"""

    def setUp(self):
        self.user = User.objects.create(
            email="test@mail.ru", password="1", is_superuser=True, is_staff=True
        )
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """test create user"""
        data = {"email": "tester@mail.ru", "password": "2"}
        response = self.client.post(reverse("users:register_user"), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_delete(self):
        """test delete user"""
        """ Test delete user """
        url = reverse("users:delete_user", args=(self.user.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_list(self):
        """test watch list of users"""
        url = reverse("users:users")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
