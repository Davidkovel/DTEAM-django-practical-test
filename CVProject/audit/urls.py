from django.urls import path
from .views import RequestLogView


urlpatterns = [
    path('logs/', RequestLogView.as_view(), name='request-logs'),
]
