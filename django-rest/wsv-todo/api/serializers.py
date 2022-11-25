from rest_framework import serializers
from todos import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todo
        fields = (
            'title',
            'id',
            'completed',
            'description',
        )
