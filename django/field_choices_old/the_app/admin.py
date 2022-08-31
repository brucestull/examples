from django.contrib import admin

from .models import NoChoices, YesChoices

admin.site.register(NoChoices)
admin.site.register(YesChoices)
