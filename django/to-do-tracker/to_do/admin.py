from django.contrib import admin

from . import models


admin.site.register(models.ToDo)
admin.site.register(models.Priority)

