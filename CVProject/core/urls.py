from django.urls import path
from django.views.decorators.cache import cache_page

from .views import CVListView, CVDetailView, cv_pdf, send_cv_pdf_view
from .translation import translate_cv

urlpatterns = [
    path('', cache_page(60 * 15)(CVListView.as_view()), name='cv_list'),
    path('cv/<int:pk>/', CVDetailView.as_view(), name='cv_detail'),
    path('cv/<int:cv_id>/translate/', translate_cv, name='translate_cv'),
    path('cv/<int:id>/pdf/', cv_pdf, name='cv_pdf'),
    path('<int:cv_id>/send-pdf/', send_cv_pdf_view, name='send_cv_pdf'),
]
