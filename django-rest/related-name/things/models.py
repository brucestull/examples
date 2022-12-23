from django.db import models
from django.contrib.auth.models import User as TheAuthUser


class Thing(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        # 'auth.User' seems to be from the 'django.contrib.auth' app ('django.contrib.auth.models').
        # 'auth.User',
        TheAuthUser,
        related_name='things',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

