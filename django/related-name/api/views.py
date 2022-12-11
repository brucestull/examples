from rest_framework import viewsets
from django.contrib.auth import get_user_model

from things.models import Thing
from .serializers import ThingSerializer, UserSerializer, UserSerializerWithThings


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserWithThingsViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializerWithThings