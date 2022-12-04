from rest_framework import viewsets

from django_app.models import AThing
from api.serializers import AThingSerializer


class AThingViewSet(viewsets.ModelViewSet):
    queryset = AThing.objects.all()
    serializer_class = AThingSerializer

