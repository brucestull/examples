from django.db import models


class AwesomeCat(models.Model):
    name = models.CharField(max_length=50)
