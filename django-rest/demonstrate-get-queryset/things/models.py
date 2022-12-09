from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(
        'auth.User',
        related_name='things',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

