from rest_framework import viewsets, generics, filters

from django.contrib.auth.models import User as DjangoUser

from . import serializers
from things import models


class ThingViewSet(viewsets.ModelViewSet):
    """
    ViewSet for a list of all things.
    """
    queryset = models.Thing.objects.all()
    serializer_class = serializers.ThingSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for a list of all users.
    """
    queryset = DjangoUser.objects.all()
    serializer_class = serializers.UserSerializer


class CurrentUserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for a list of one user, the current user.
    """
    queryset = DjangoUser.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)


class CurrentUserView(generics.RetrieveAPIView):
    """
    View for a single user, the current user.
    """
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user


# # GitHub suggestion:
# class ThingSearchView(generics.ListAPIView):
#     serializer_class = serializers.ThingSerializer

#     def get_queryset(self):
#         return models.Thing.objects.filter(name__icontains=self.request.query_params.get('q', ''))

class ThingDescriptionSearchView(generics.ListAPIView):
    """
    ListAPIView for a list of things, filtered by description.
    """
    queryset = models.Thing.objects.all()
    serializer_class = serializers.ThingSerializer
    search_fields = ['description']
    filter_backends = [
        filters.SearchFilter
    ]


class ThingNameSearchView(generics.ListAPIView):
    """
    ListAPIView for a list of things, filtered by name.
    """
    queryset = models.Thing.objects.all()
    serializer_class = serializers.ThingSerializer
    search_fields = ['name']
    filter_backends = [
        filters.SearchFilter
    ]


