from django.shortcuts import render

from rest_framework import viewsets, permissions, status

from .models import Place, Route
from .serializers import PlaceSerializer, RouteSerializer
from trip.models import Trip

from rest_framework import serializers


class RouteViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Place.objects.none()
    permission_classes = [permissions.AllowAny]
    
    def perform_create(self, serializer):
        trip_id = self.kwargs.get('trip_id')
        trip = Trip.objects.get(id=trip_id)
        serializer.save(author=self.request.user, trip=trip)

    def get_queryset(self):
        trip_id = self.kwargs.get('trip_id')
        return Route.objects.filter(trip__id=trip_id)
    

class PlacesViewSet(viewsets.ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.none()
    permission_classes = [permissions.AllowAny]
    
    def perform_create(self, serializer):
        route_id = self.kwargs.get('route_id')
        route = Route.objects.get(id=route_id)
        serializer.save(route=route)
        
    def get_queryset(self):
        route_id = self.kwargs.get('route_id')
        return Place.objects.filter(route__id=route_id)
    

    