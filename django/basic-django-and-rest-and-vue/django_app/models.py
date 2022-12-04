from django.db import models


class AThing(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        'auth.User',
        related_name='things',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
