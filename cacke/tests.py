from django.test import TestCase

import conf


class Cacke(TestCase):
    def test_config_sphinx(self):
        self.assertEqual(conf.author, 'ah8ad3')
