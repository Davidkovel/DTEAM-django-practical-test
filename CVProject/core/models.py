from django.db import models


# Create your models here.


class Skill(models.Model):
    name = models.CharField(max_length=60)
    proficiency = models.CharField(max_length=60,
                                   help_text="Enter your proficiency level (e.g., Beginner, Intermediate, Advanced)")
    description = models.TextField(help_text="Describe your skill in detail")


class Project(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(help_text="Describe your project in detail")
    link = models.URLField(help_text="Enter the URL to your project")
    technologies_used = models.CharField(max_length=60, help_text="List the technologies used in this project")


class CV(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    skills = models.ManyToManyField(Skill, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    bio = models.TextField(help_text="Write a short bio about yourself")
    contacts = models.CharField(max_length=60, help_text="Enter your contact information")
