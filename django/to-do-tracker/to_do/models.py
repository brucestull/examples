from django.db import models


class Priority(models.Model):
    description = models.CharField(max_length=255)
    priority_level = models.IntegerField()
    
    def __str__(self):
        return str(self.priority_level) + ' : ' + self.description


class ToDo(models.Model):
    description = models.CharField(max_length=255)
    # `PROTECT` prevents deletion of `Priority` instance if
    #     it is associated with a `ToDo` instance.
    priority = models.ForeignKey(Priority, on_delete=models.PROTECT)

    def __str__(self):
        return self.description + ' : ' + self.priority.description
