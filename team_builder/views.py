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


class HomeView(generic.ListView):
    model = Project
    template_name = 'index.html'
    context_object_name = 'project_home'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('s')
        if search_term:
            queryset = queryset.filter(
                Q(title__icontains=search_term) |
                Q(description__icontains=search_term)
            )

        return queryset