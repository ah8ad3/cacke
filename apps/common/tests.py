from django.test import TestCase
from django.urls import reverse


class Common(TestCase):
    def test_call_view_loads(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
