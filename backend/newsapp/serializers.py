from rest_framework import serializers
from . import models

class NewsArticleSerializer(serializers.ModelSerializer):
    class Meta :
        model = models.NewsArticle
        fields = '__all__'
