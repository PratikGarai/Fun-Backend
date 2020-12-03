from rest_framework import generics
from . import models
from . import serializers
import json
from rest_framework.response import Response
from django.http import JsonResponse


class TaskList(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoTaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoTaskSerializer

def markDone(request, pk):
    d = None
    try:
        m = models.Todo.objects.all().filter(pk=pk)[0]
        m.isComplete = True
        m.save()
        d = {"message":"success"}
    except :
        d = {"message":"failed to change state"}
    return JsonResponse(d)

def markUndone(request, pk):
    d = None
    try:
        m = models.Todo.objects.all().filter(pk=pk)[0]
        m.isComplete = False
        m.save()
        d = {"message":"success"}
    except :
        d = {"message":"failed to change state"}
    return JsonResponse(d)
