from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm
from .models import CustomUser


class SignUpView(CreateView):
    """
    View for signing up a new user.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserListView(ListView):
    """
    View for listing all users.
    """
    model = CustomUser
    template_name = 'users.html'
    context_object_name = 'users'

