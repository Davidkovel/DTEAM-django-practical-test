from django.db import models

from enum import Enum


class HttpMethod(models.TextChoices):
    GET = 'GET', 'GET'
    POST = 'POST', 'POST'
    PUT = 'PUT', 'PUT'
    DELETE = 'DELETE', 'DELETE'


class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10, choices=HttpMethod.choices, default=HttpMethod.GET)
    path = models.CharField(max_length=255)
    query_params = models.JSONField(null=True, blank=True)
    remote_ip_address = models.GenericIPAddressField()

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Request Log'
        verbose_name_plural = 'Request Logs'

    def __str__(self):
        return f"{self.method} {self.path} - {self.response_code}"
