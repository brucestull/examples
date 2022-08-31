from django.db import models


class NoChoices(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class YesChoices(models.Model):
    name = models.CharField(max_length=20)

    THE_CHOICES = [
        ('FRST', 'First'),
        ('SCND', 'Second'),
    ]

    the_specific_choice = models.CharField(
        choices=THE_CHOICES,
        max_length=4,
        null=True,
        default='FRST',
    )

    def __str__(self):
        return self.name