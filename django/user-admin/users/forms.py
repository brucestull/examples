from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'is_candidate',
            'is_recruiter',
        )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'is_candidate',
            'is_recruiter',
        )