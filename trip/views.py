from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from .models import Trip, NeededList, Item
from .serializers import TripSerializer, NeededListSerializer, ItemSerializer, TripSerializerWithItems



class TripViewSet(viewsets.ModelViewSet):
    serializer_class = TripSerializer
    queryset = Trip.objects.all()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    def get_queryset(self):
        return Trip.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['GET'])
    def with_items(self, request, pk=None):
        trip = self.get_object()
        serializer = TripSerializerWithItems(trip)
        return Response(serializer.data)
    
    @action(detail=True, methods=['POST'])
    def assign_list_to_trip(self, request, pk=None):
        trip = self.get_object()
        needed_list_id = request.data.get('needed_list_id')
        needed_list = get_object_or_404(NeededList, pk=needed_list_id)
        
        trip.item_list= needed_list
        trip.save()
        
        return Response({'status': 'Lista dodana do wycieczki'}, status=status.HTTP_200_OK)
    
    
class NeededListViewSet(viewsets.ModelViewSet):
    serializer_class = NeededListSerializer
    queryset = NeededList.objects.none()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return NeededList.objects.filter(user=self.request.user)
    
    @action(detail=True, methods=['POST'])
    def add_and_create_item(self, request, pk=None):
        needed_list = self.get_object()
        name = request.data.get('name')
        
        item = Item.objects.create(
            name = name
        )
        needed_list.items.add(item)
        needed_list.save()
        return Response({'status': 'Przedmiot dodany'}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['POST'])
    def change_packed_and_unpacked(self, request, pk=None):
        needed_list = self.get_object()
        item_id = request.data.get('item_id')
        item = get_object_or_404(Item, pk=item_id)
        
        item.packed = not item.packed
        item.save()
 
        
        return Response({'status': 'Zmieniona stan'}, status=status.HTTP_200_OK)
            
            
