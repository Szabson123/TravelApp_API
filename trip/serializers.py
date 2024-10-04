from rest_framework import serializers

from .models import Trip, NeededList, Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']
        

class NeededListSerializer(serializers.ModelSerializer):
    items = ItemListSerializer(many=True, read_only=True, source='items')

    class Meta:
        model = NeededList
        fields = ['id', 'name', 'items']
    
    
class TripSerializers(serializers.ModelSerializer):
    items_list = NeededListSerializer(many=True, source='item_list')

    class Meta:
        model = Trip
        fields = ['id', 'name', 'items_list'] 