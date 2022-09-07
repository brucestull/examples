from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100, null=False)
    priority = models.ForeignKey('Priority', on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' : ' + self.text + ' : ' + self.priority.name

class Priority(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} : {self.name}"



