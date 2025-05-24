from django.db.models import Prefetch

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template
from rest_framework import viewsets, generics
from xhtml2pdf import pisa

from django.views.generic import ListView, DetailView
from .models import CV, Skill, Project
from .serializers import CVSerializer
from .tasks import send_cv_pdf


class CVListView(ListView):
    model = CV
    template_name = 'core/cv_list.html'
    context_object_name = "cv_list"
    paginate_by = 10

    def get_queryset(self):
        return CV.objects.prefetch_related(
            Prefetch('skills', queryset=Skill.objects.all()),
            Prefetch('projects', queryset=Project.objects.all())
        ).all()


class CVDetailView(DetailView):
    model = CV
    template_name = 'core/cv_detail.html'
    context_object_name = "cv"

    def get_queryset(self):
        return CV.objects.prefetch_related(
            Prefetch('skills', queryset=Skill.objects.all()),
            Prefetch('projects', queryset=Project.objects.all())
        ).all()


def cv_pdf(request, id):
    cv = CV.objects.get(pk=id)
    template = get_template('core/cv_pdf.html')
    html = template.render({'cv': cv})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cv_{cv.id}.pdf"'
    pisa.CreatePDF(html, dest=response)
    return response


class CVListCreate(generics.ListCreateAPIView):  # GET / POST
    queryset = CV.objects.all()
    serializer_class = CVSerializer


class CVRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):  # GET/PUT/PATCH/DELETE  WITH ID
    queryset = CV.objects.all()
    serializer_class = CVSerializer


def send_cv_pdf_view(request, cv_id):
    if request.method == 'POST':
        email = request.POST.get('email')
        send_cv_pdf.delay(cv_id, email)
        return redirect('cv_detail', pk=cv_id)