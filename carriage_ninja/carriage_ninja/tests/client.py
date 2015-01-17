from django.utils import unittest
from django.test.client import Client

from django.core.urlresolvers import reverse

from carriage_ninja import settings


class BasicClientTests(unittest.TestCase):
    fixtures = [
        'users.json'
    ]

    def test_index(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_can_load_login_page(self):
        client = Client()
        response = client.get(settings.LOGIN_URL)
        self.assertEqual(response.status_code, 200)

    def test_can_log_in(self):
        client = Client()
        response = client.post(settings.LOGIN_URL)
        self.assertEqual(response.status_code, 200)

    def test_can_view_profile(self):
        client = Client()
        response = client.get(reverse(''))
        self.assertEqual(response.status_code, 200)

    def test_can_log_out(self):
        client = Client()
        response = client.get(settings.LOGOUT_URL)
        self.assertEqual(response.status_code, 200)
