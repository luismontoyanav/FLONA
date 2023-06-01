from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework.views import status
from users.models import Employee


class ListEmployeesApiView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("employees")

    def test_list_employees(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
