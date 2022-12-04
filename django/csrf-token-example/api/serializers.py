from rest_framework import serializers

from things.models import Thing


class ThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Thing
        fields = (
            'name',
            'created_at',
            'updated_at',
        )