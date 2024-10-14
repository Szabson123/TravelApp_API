from rest_framework import serializers

from .models import Trip, NeededList, Item

from money.serializers import TripBudgetSerializer

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'packed']
        

class NeededListSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True, read_only=True, source='items')
    user = serializers.ReadOnlyField(source='user.email')
    
    class Meta:
        model = NeededList
        fields = ['id', 'name', 'item', 'user']
    
    
class TripSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    budget = TripBudgetSerializer()

    class Meta:
        model = Trip
        fields = ['id', 'name', 'user', 'budget']
        read_only_fields = ['user']
