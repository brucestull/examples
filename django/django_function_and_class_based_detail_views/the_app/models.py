from django.db import models


class StringValue(models.Model):
    """
    Model representing the `StringValue` which will be used to display a list on webpage.
    """
    name = models.CharField(
        max_length=10,
        verbose_name='verbose_name for the StringValue',
    )

    def __str__(self):
        """
        String representation for the `StringValue` object.
        """
        string_value = f"{self.id} : {self.name}"
        return string_value
