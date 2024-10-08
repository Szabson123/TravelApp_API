from rest_framework import serializers

from .models import Trip, NeededList, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']
        

class NeededListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True, source='items')

    class Meta:
        model = NeededList
        fields = ['id', 'name', 'items']
    
    
class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = ['id', 'name', 'user']
