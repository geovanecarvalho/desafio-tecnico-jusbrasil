from django.test import TestCase


class ApiRoot(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_link_api_v1_jtal(self):
        expected = "api/v1/jtal/"
        self.assertContains(self.response, expected)



