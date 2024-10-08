from rest_framework import serializers

from .models import Trip, NeededList, Item
from user.serializers import UserSerializer

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name']
        

class NeededListSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    
    class Meta:
        model = NeededList
        fields = ['id', 'name', 'item']
    
    
class TripSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Trip
        fields = ['id', 'name', 'user']