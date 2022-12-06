from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserDetailView(UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = 'registration/user_detail.html'
    context_object_name = 'custom_user'

    def test_func(self):
        return self.request.user.is_recruiter == True


class UserEditView(UpdateView):
    model = CustomUser
    template_name = 'registration/edit_user.html'
    fields = [
        'username',
        'email',
        'is_candidate',
        'is_recruiter',
    ]