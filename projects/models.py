from django.conf import settings
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=140)

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
    skill = models.ForeignKey(Skill)
    position = models.ForeignKey(Position)

    def __str__self(self):
        return self.title




