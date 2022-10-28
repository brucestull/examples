from django.db import models


class TheThing(models.Model):
    attribute_01 = models.CharField(max_length=20)
    attribute_02 = models.CharField(max_length=20)

    def __str__(self):
        return self.attribute_01 + ' : ' + self.attribute_02

