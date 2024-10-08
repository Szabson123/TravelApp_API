from rest_framework import serializers

from .models import Trip, NeededList, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']
        

class NeededListSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True, source='items')
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = NeededList
        fields = ['id', 'name', 'items', 'user']
    
    
class TripSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Trip
        fields = ['id', 'name', 'user']
        read_only_fields = ['user']
