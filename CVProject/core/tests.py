from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

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

class CVApiTests(APITestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'bio': 'Developer',
            'contacts': 'john@example.com',
        }
        self.invalid_data = {
            'first_name': '',
            'last_name': 'Doe',
            'bio': 'Developer',
            'contacts': 'invalid-email'
        }
        self.cv = CV.objects.create(**self.valid_data)

    def test_get_cv_list(self):
        response = self.client.get(reverse('cv-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_valid_cv(self):
        response = self.client.post(
            reverse('cv-list'),
            data=self.valid_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CV.objects.count(), 2)

    def test_create_invalid_cv(self):
        response = self.client.post(
            reverse('cv-list'),
            data=self.invalid_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_single_cv(self):
        response = self.client.get(
            reverse('cv-detail', kwargs={'pk': self.cv.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.cv.first_name)

    def test_update_cv(self):
        updated_data = {'bio': 'Updated bio info'}
        response = self.client.patch(
            reverse('cv-detail', kwargs={'pk': self.cv.pk}),
            data=updated_data,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.cv.refresh_from_db()
        self.assertEqual(self.cv.bio, 'Updated bio info')

    def test_delete_cv(self):
        response = self.client.delete(
            reverse('cv-detail', kwargs={'pk': self.cv.pk})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CV.objects.count(), 0)


# ----------------------------------------------------------------------
# Ran 8 tests in 0.063s
#
# OK
