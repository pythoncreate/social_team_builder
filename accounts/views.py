from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView

from .forms import UserProfileForm

from . import models

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


class ProfileView(generic.ListView):
    model = models.UserProfile
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        profile = models.UserProfile.objects.all()
        context['profile'] = profile

        return context


class EditProfileView(generic.UpdateView):
    model = models.UserProfile
    template_name = "accounts/profile_edit.html"


class SignUp(generic.CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


# @login_required
# def view_profile(request):
#     profile = request.user.userprofile
#     return render(request, 'accounts/profile.html', {'profile':profile})
#
# @login_required
# def edit_profile(request):
#     user = request.user
#     if request.method == 'POST':
#         form = forms.EditProfileForm(data=request.POST, files=request.FILES, instance=user.userprofile)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/profile')
#         else:
#             return render(request, 'accounts/profile.html', {'form':form})
#     else:
#         form = forms.EditProfileForm(instance=user.userprofile)
#         args = {'form':form}
#         return render(request, 'accounts/profile.html', args)
#
# @login_required
# def change_password(request):
#     if request.method == 'POST':
#         form = PasswordChangeForm(data=request.POST, user=request.user)
#
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request,form.user)
#             return redirect('/accounts/profile')
#
#     else:
#         form = PasswordChangeForm(user=request.user)
#         args = {'form': form}
#         return render(request, 'accounts/change_password.html', args)
#
# @property
# def image_url(self):
#     if self.image and hasattr(self.image, 'url'):
#         return self.image.url
#
