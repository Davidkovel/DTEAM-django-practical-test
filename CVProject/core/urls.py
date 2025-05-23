from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CVListView, CVDetailView

urlpatterns = [
    path('', cache_page(60*15)(CVListView.as_view()), name='cv_list'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail')
]
