from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class CustomUser(AbstractUser):
    is_candidate = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    
    pass
    # add additional fields in here

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})
    