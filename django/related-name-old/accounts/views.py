from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class CurrentUserView(generic.DetailView):
    model = get_user_model()
    template_name = 'home.html'

    def get_object(self):
        return self.request.user
