from django.test import TestCase
from .models import Crawler
from rest_framework.test import APITestCase
from rest_framework import status


class ApiRoot(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_link_api_v1_jtal(self):
        expected = "api/v1/jtal/"
        self.assertContains(self.response, expected)
