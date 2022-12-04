from rest_framework import serializers

from django_app.models import AThing


class AThingSerializer(serializers.ModelSerializer):

    class Meta:
        model = AThing
        fields = (
            'name',
            'user',
        )