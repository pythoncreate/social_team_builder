from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save

from projects.models import Skill, Project


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email,
            username,
            password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True, default='')
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return "@{}".format(self.username)

    def get_short_name(self):
        return self.username

    def get_long_name(self):
        return "@{} ({})".format(self.username, self.email)


class UserProfile(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    first_name = models.CharField(max_length=40, default='', blank=True)
    last_name = models.CharField(max_length=40, default='', blank=True)
    bio = models.TextField(blank=True, default='')
    avatar = models.ImageField(upload_to='')
    skills = models.ManyToManyField(Skill)
    projects = models.ManyToManyField(Project)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)