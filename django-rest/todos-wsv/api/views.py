# from rest_framework import generics
from rest_framework import viewsets

from todos import models
from . import serializers


# class TodoList(generics.ListCreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer


# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = serializers.TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer