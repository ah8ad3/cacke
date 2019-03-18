from django.test import TestCase

import conf
import manage
from cacke import wsgi
from cacke.settings.celery import debug_task
from cacke.settings import pro


class Cacke(TestCase):
    def test_config_sphinx(self):
        self.assertEqual(conf.author, 'ah8ad3')

    def test_wsgi_module(self):
        self.assertIsNotNone(wsgi.application, 'check wsgi is not nil')

    def test_manage_module(self):
        self.assertIsNotNone(manage, 'check main manage is not nil')

    def test_celery_app_task(self):
        self.assertIsNotNone(debug_task.apply(), 'check task not empty')

    def test_pro_settings(self):
        self.assertIsNotNone(pro, 'pro is not none')
