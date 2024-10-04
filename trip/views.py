from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trip, NeededList, ItemList
from .serializers import TripSerializers, NeededListSerializer, ItemListSerializer


class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemListSerializer
    queryset = ItemList.objects.none()
    
    def get_queryset(self):
        needed_list_id = self.kwargs['needed_list_pk']
        tript_id =self.kwargs['trip_pk']
        return NeededList.objects.filter(tript_id=tript_id, needed_list_id=needed_list_id)
    