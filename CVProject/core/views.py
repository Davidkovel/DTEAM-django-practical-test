from django.db.models import Prefetch
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import CV, Skill, Project


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
