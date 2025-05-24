from django.urls import path
from .views import RequestLogView, SettingsView


urlpatterns = [
    path('logs/', RequestLogView.as_view(), name='request-logs'),
    path('settings/', SettingsView.as_view(), name='settings'),
]
