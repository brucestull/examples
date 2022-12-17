from django.urls import reverse_lazy
from django.views import generic

from .forms import UserCreationFormWithEmail


class SignUpView(generic.CreateView):

    form_class = UserCreationFormWithEmail
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"