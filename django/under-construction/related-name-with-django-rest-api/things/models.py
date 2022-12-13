from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        'auth.User',
        related_name='owner_related_name_for_things',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id) + ' : ' + self.name + ' : ' + self.owner.username
