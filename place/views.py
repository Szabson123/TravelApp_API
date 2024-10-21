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
        serializer.save(author=self.request.user)

    def get_queryset(self):
        trip_id = self.request.query_params.get('trip_id') or self.request.data.get('trip_id')
        if not trip_id:
            return Route.objects.none()
        
        try:
            trip = Trip.objects.get(id=trip_id)
        except Trip.DoesNotExist:
            return Route.objects.none()
        return Route.objects.filter(author=self.request.user, trip=trip)