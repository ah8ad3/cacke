from django.test import TestCase
from django.urls import reverse
from django.apps import apps

from .apps import CommonConfig
from .tasks import add


class Common(TestCase):
    def test_call_view_loads(self):
        response = self.client.get(reverse('welcome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_apps_file(self):
        self.assertEqual(CommonConfig.name, 'apps.common')
        self.assertEqual(apps.get_app_config('common').name, 'apps.common')

    def test_tasks_file(self):
        self.assertEqual(add.apply(args=(5, 6)).get(), 11)
