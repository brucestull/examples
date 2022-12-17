from django.db import models


class Thing(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name + ' : ' + self.description
