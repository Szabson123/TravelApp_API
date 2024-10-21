from rest_framework import serializers

from .models import Route, Place
from trip.models import Trip

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'name', 'description']


class RouteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user.email')
    trip = serializers.PrimaryKeyRelatedField(queryset=Trip.objects.all()) 
    places = PlaceSerializer(many=True, read_only=True)
    trip_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Route
        fields = ['id', 'name', 'description', 'author', 'trip', 'places', 'trip_name']
        
    def get_trip_name(self, obj):
        return obj.trip.name
    

class RouteToTripSerialzier(serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Route
        fields = ['id', 'name', 'description', 'places']
