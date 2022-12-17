from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from things.models import Thing
from api.serializers import ThingSerializer


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('-id')
    serializer_class = ThingSerializer
    permission_classes = [IsAuthenticated]
