from rest_framework import viewsets, generics

from django.contrib.auth.models import User as DjangoUser

from . import serializers
from things import models


class ThingViewSet(viewsets.ModelViewSet):
    queryset = models.Thing.objects.all()
    serializer_class = serializers.ThingSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = DjangoUser.objects.all()
    serializer_class = serializers.UserSerializer


class CurrentUserViewSet(viewsets.ModelViewSet):
    queryset = DjangoUser.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user