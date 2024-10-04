from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Trip, NeededList, Item
from .serializers import TripSerializers, NeededListSerializer, ItemListSerializer


class ItemListViewSet(viewsets.ModelViewSet):
    serializer_class = ItemListSerializer

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