from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        'id',
        'email',
        'username',
        'is_candidate',
        'is_recruiter',
        'is_manager',
        'is_whatever',
    ]

admin.site.register(CustomUser, CustomUserAdmin)