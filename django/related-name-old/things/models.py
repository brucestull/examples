from django.db import models


class Thing(models.Model):
    """
    Model representing a thing.
    """
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(
        'auth.User',
        related_name='things',
        # `CASCADE` means that if the `accounts.User` is deleted, all of
        # their `things` will be deleted as well.
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.id) + ' : ' + self.name + ' : ' + self.owner.username
