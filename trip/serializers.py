from rest_framework import serializers

from .models import Trip, NeededList, Item

from money.serializers import TripBudgetSerializer
from money.models import TripBudget

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
    
#CRUD 
class TripSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    budget = TripBudgetSerializer(read_only=True)

    class Meta:
        model = Trip
        fields = ['id', 'name', 'user', 'budget', 'country']
        read_only_fields = ['user']


#Read
class TripSerializerWithItems(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    budget = TripBudgetSerializer()
    item_list = NeededListSerializer()
    class Meta:
        model = Trip
        fields = ['id', 'name', 'user', 'budget', 'item_list', 'country']
        read_only_fields = ['user']