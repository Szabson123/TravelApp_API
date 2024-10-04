from rest_framework import serializers

from .models import Trip, NeededList, ItemList


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemList
        fields = ['id', 'name']
        

class NeededListSerializer(serializers.ModelSerializer):
    item = ItemListSerializer(many=True)
    
    class Meta:
        model = NeededList
        fields = ['id', 'name', 'item']
    
    
class TripSerializers(serializers.ModelSerializer):
    items_list = NeededListSerializer
    
    class Meta:
        model = Trip
        fields = ['id', 'name', 'item_list']