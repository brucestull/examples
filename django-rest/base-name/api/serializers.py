from rest_framework import serializers
from django.contrib.auth.models import User as DjangoUser

from things import models


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Thing
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    things = ThingSerializer(many=True, read_only=True)

    class Meta:
        model = DjangoUser
        fields = [
            'id',
            'username',
            'things',
        ]