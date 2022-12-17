from rest_framework import viewsets
from django.contrib.auth import get_user_model

from api import serializers
from things.models import Thing


class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = serializers.ThingSerializer

    def get_queryset(self):
        print()
        print('self.get_view_name(): ', self.get_view_name())
        return super().get_queryset()


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer


class ZeCurrentUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = serializers.CurrentUserSerializer

    def get_queryset(self):
        print()
        # print(dir(self))
        # print('dir(self.get_view_name()): ', dir(self.get_view_name()))
        print('self.get_view_name(): ', self.get_view_name())
        # print(self.queryset)
        # print(self.request.user)
        return self.queryset.filter(id=self.request.user.id)
