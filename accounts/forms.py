from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from . import models


User = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ["email", "username", "password1", "password2"]
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'bio',
            'avatar',
        ]


class EditProfileForm(forms.ModelForm):
    verify_email = forms.EmailField(label = "Please verify email address")
    bio = forms.CharField(widget=forms.Textarea, min_length=10)

    class Meta:
        model = models.UserProfile
        fields = [
            'first_name',
            'last_name',
            'email',
            'verify_email',
            'bio',
            'avatar',
        ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        verify = cleaned_data['verify_email']
        if email != verify:
            raise forms.ValidationError(
                "You need to enter same email in both fields."
            )

    def  clean_birth_date(self):
        date_birth = self.cleaned_data['date_birth']