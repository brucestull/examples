from django.db import models


class AwesomeCat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(thine_fuzzy_self):
        return f"{thine_fuzzy_self.id} : {thine_fuzzy_self.name}"
