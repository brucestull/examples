from django.db import models


class NameWithChoices(models.Model):
    
    name = models.CharField(
        max_length=20,
    )
    
    THE_CHOICES = [
        ('FRST', 'First'),
        ('SCND', 'Second'),
    ]

    the_specific_choice = models.CharField(
        choices=THE_CHOICES,
        max_length=4,
        default='FRST',
    )

    def __str__(self):
        return self.name
