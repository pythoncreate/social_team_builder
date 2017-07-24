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

from .forms import UserProfileForm

from . import models

from projects import models as m

from . import forms


class LoginView(generic.FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
    template_name = "accounts/signin.html"

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(self.request, **self.get_form_kwargs())

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)


class LogoutView(generic.RedirectView):
    url = reverse_lazy("home")

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'accounts/profile.html'
    login_url = settings.LOGIN_REDIRECT_URL

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        lookup = kwargs.get('username')
        user = models.User.objects.get(username=lookup)
        profile = models.UserProfile.objects.prefetch_related('skills').get(user=user)
        context['profile'] = profile
        context['skills'] = [skill for skill in profile.skills.all()]

        positions = m.Position.objects.all()
        context['positions'] = positions.filter(Q(project__owner=user)& Q(project__complete=True))

        projects = models.Project.objects.all()
        context['current_projects'] = projects.filter(Q(owner=user) & Q(complete=False))
        context['past_projects'] = projects.filter(Q(owner=user) & Q(complete=True))
        return context


class EditProfileView(LoginRequiredMixin,generic.UpdateView):
    model = models.UserProfile
    template_name = "accounts/profile_edit.html"
    form_class = forms.EditProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['p_formset'] = PositionInlineFormSet(
            queryset=Position.objects.filter(project=context['project']),
            prefix='p_formset'
        )
        return context


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


