from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserCreationFormWithEmail(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email'
        ]