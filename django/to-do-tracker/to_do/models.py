from django.db import models


class Priority(models.Model):
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description


class ToDo(models.Model):
    description = models.CharField(max_length=255)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
