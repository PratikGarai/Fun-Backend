from rest_framework import serializers

from . import models

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemImage
        fields = '__all__'

class GetItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True)
    class Meta:
        model = models.Item
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Item
        fields = '__all__'
