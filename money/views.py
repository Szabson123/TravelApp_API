from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status

from .models import TripBudget
from .serializers import TripBudgetSerializer


class TripBudgetViewSet(viewsets.ModelViewSet):
    serializer_class = TripBudgetSerializer
    queryset = TripBudget.objects.all()
    
    