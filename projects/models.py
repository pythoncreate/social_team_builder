from django.conf import settings
from django.db import models


class Skill(models.Model):
    """User skills class."""
    ANDROID = 1
    DESIGNER = 2
    JAVA = 3
    PHP = 4
    PYTHON = 5
    RAILS = 6
    WORDPRESS = 7
    IOS = 8

    SKILL_CHOICES = (
        (str(ANDROID), 'Android Developer'),
        (str(DESIGNER), 'Designer'),
        (str(JAVA), 'Java Developer'),
        (str(PHP), 'PHP Developer'),
        (str(PYTHON), 'Python Developer'),
        (str(RAILS), 'Rails Developer'),
        (str(WORDPRESS), 'Wordpress Developer'),
        (str(IOS), 'iOS Developer')
    )

    name = models.CharField(max_length=140, choices=SKILL_CHOICES, default='unknown')

    def __str__self(self):
        return self.name


class Position(models.Model):
    title = models.CharField(max_length=140)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="position")
    description = models.TextField()
    filled = models.BooleanField(default=False)

    def __str__self(self):
        return self.title


class Project(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="project")
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    skill = models.ForeignKey(Skill, default="java")

    def __str__self(self):
        return self.title




