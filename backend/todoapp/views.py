from rest_framework import generics
from . import models
from . import serializers

class TaskList(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoTaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoTaskSerializer
