from django.db import models

from config.settings import AUTH_USER_MODEL


class Priority(models.Model):
    description = models.CharField(max_length=255)
    priority_level = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.priority_level) + ' : ' + self.description


class ToDo(models.Model):
    description = models.CharField(max_length=255)
    # `PROTECT` prevents deletion of `Priority` instance if
    #     it is associated with a `ToDo` instance.
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True, null=True)
    person = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name='todos',
        # `CASCADE` allows deletion of `AUTH_USER_MODEL` [`CustomUser`] instance and
        #     also does a cascading deletion of `ToDo` instance.
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.person.username + ' : ' + self.description + ' : ' + self.priority.description
