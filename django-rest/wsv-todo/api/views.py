from rest_framework import viewsets

from todos import models
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


# #### Alternate code for TodoViewSet ####
# from rest_framework import generics

# class TodoList(generics.ListCreateAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer

# class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Todo.objects.all()
#     serializer_class = TodoSerializer
# ########################################