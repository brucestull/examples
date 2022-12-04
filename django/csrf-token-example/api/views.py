from rest_framework import viewsets

from things.models import Thing
from api.serializers import ThingSerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
