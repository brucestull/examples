from rest_framework import serializers
from django.contrib.auth import get_user_model

from things.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = (
            'id',
            'name',
            'owner'
        )


class NestedThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = (
            'id',
            'name',
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
        )


class UserSerializerWithThings(serializers.ModelSerializer):
    things = NestedThingSerializer(
        many=True,
        read_only=True,
        source='owner_related_name_for_things',
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'things',
        )
