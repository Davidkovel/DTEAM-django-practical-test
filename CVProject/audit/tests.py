from django.test import TestCase, Client
from django.urls import reverse
from CVProject.audit.models import RequestLog


class RequestLoggingTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_request_logging(self):
        response = self.client.get('/api/audit/logs/')
        self.assertEqual(response.status_code, 200)
