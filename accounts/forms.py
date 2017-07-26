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
            'bio',
            'avatar',
        ]


class EditProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'First name',
            'class': ''
        })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Last name',
            'class': ''
        })
    )
    bio = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Tell us about yourself...',
            'class': ''
        })

    )
    avatar = forms.ImageField(
        label='Avatar',
        required=False,
        widget=forms.FileInput(attrs={
            'class': ''
        })
    )
    skills = forms.ModelMultipleChoiceField(
        queryset=models.Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'size': 20}),
        required=False,
        label=''
    )


    class Meta:
        model = models.UserProfile
        fields = ['first_name', 'last_name', 'bio', 'avatar', 'skills']
