from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CVListView, CVDetailView, cv_pdf



urlpatterns = [
    path('', cache_page(60*15)(CVListView.as_view()), name='cv_list'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
    path('cv/<int:id>/pdf/', cv_pdf, name='cv_pdf'),
]
