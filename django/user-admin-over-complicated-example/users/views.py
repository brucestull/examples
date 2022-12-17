from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    # context_object_name = 'custom_users'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'custom_user'


class UserEditView(UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'edit_user.html'
    fields = [
        'username',
        'email',
        'is_candidate',
        'is_recruiter',
        'is_manager',
        'is_whatever',
    ]

    def test_func(self):
        return self.request.user.is_manager == True


class WhateverCanView(UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'edit_user.html'
    fields = [
        'username',
        'email',
        'is_candidate',
        'is_recruiter',
        'is_manager',
        'is_whatever',
    ]

    def test_func(self):
        return self.request.user.is_whatever == True


class RecruiterCanView(UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'edit_user.html'
    fields = [
        'username',
        'email',
        'is_candidate',
    ]

    def test_func(self):
        return self.request.user.is_recruiter == True

