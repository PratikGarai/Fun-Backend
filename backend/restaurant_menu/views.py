from rest_framework import generics

from . import models
from . import serializers

class ItemList(generics.ListCreateAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.GetItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Item.objects.all()
    serializer_class = serializers.GetItemSerializer