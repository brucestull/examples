from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey('auth.User', related_name='things', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + " : " + self.name + " : " + self.owner.username