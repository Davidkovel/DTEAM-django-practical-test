from django.test import TestCase
from django.urls import reverse

from .models import CV, Skill, Project


class CVTest(TestCase):
    def setUp(self):
        self.skills = Skill.objects.create(
            name="Python",
            proficiency="Advanced",
            description="Expert in Python programming language"
        )

        self.projects = Project.objects.create(
            title="Django Project",
            description="A web application built with Django",
            link="http://example.com",
            technologies_used="Django, Python, JavaScript"
        )

        self.cv = CV.objects.create(
            first_name="Test",
            last_name="User",
            bio="Test bio",
            contacts="test@example.com"
        )

        self.cv.skills.set([self.skills])
        self.cv.projects.set([self.projects])

    def test_cv_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/cv_list.html')

    def test_cv_detail_view(self):
        response = self.client.get(reverse('cv_detail', args=[self.cv.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'core/cv_detail.html')



# ----------------------------------------------------------------------
# Ran 2 tests in 0.036s
#
# OK
