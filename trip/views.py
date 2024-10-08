from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Trip, NeededList, Item
from .serializers import TripSerializer, NeededListSerializer, ItemSerializer


class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
    

class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.none()
    
    def get_queryset(self):
        needed_list_id = self.kwargs['needed_list_pk']
        tript_id =self.kwargs['trip_pk']
        return NeededList.objects.filter(tript_id=tript_id, needed_list_id=needed_list_id)
    