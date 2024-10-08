from django.shortcuts import render, get_object_or_404

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
    
    
class NeededListViewSet(viewsets.ModelViewSet):
    serializer_class = NeededList
    queryset = NeededList.objects.none()
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return NeededList.objects.filter(user=self.request.user)
    

class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.none()
    
    def get_queryset(self):
        needed_list_id = self.kwargs['needed_list_pk']
        return Item.objects.filter(items__id=needed_list_id)

    def create(self, request, *args, **kwargs):
        needed_list_id = self.kwargs.get('needed_list_pk')
        neededlist = get_object_or_404(NeededList, pk=needed_list_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        item = serializer.save()
        neededlist.item.add(item)

        return Response(serializer.data, status=status.HTTP_201_CREATED)