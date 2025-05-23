from django.urls import path
from .views import CVListCreate, CVRetrieveUpdateDestroy

urlpatterns = [
    path('cv/', CVListCreate.as_view(), name='cv-list'),
    path('cv/<int:pk>/', CVRetrieveUpdateDestroy.as_view(), name='cv-detail'),
]