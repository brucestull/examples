from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser

from things import models


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thing
        fields = [
            'id',
            'name',
            'description',
            'owner',
            'created',
            'updated',
        ]

class UserSerializer(serializers.ModelSerializer):
    things = ThingSerializer(many=True, read_only=True)

    class Meta:
        model = DjangoUser
        fields = [
            'id',
            'username',
            'things',
        ]