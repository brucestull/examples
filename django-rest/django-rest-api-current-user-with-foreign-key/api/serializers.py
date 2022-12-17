from rest_framework import serializers
from django.contrib.auth import get_user_model

from things.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Thing
            fields = [
                'id',
                'name',
                'owner',
            ]


class NestedThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thing
        fields = [
            'id',
            'name',
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'email',
            'is_staff',
            'is_superuser',
        )


class CurrentUserSerializer(serializers.ModelSerializer):
    things_detail = NestedThingSerializer(
        source='things',
        many=True,
        read_only=True,
    )

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'things_detail',
        )
