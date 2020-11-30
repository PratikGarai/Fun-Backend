from rest_framework import generics
from . import models
from . import serializers

class NewsArticleList(generics.ListCreateAPIView):
    queryset = models.NewsArticle.objects.all()
    serializer_class = serializers.NewsArticleSerializer

class NewsArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.NewsArticle.objects.all()
    serializer_class = serializers.NewsArticleSerializer
