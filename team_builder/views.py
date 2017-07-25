from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView
from django.db.models import Q
from django.conf import settings
from django.views.generic.edit import UpdateView


from projects import models as m

from projects.models import *
from accounts.models import *


class ProjectListView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        projects = Project.objects.all()
        context['current_projects'] = projects.filter(Q(complete=False))
        positions = Position.objects.all()
        context['positions'] = positions.filter(project=context['current_projects'])
        return context