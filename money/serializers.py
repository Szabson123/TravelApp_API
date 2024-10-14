from rest_framework import serializers
from .models import TripBudget, TripBudgetItemMinus, TripBudgetItemPlus


class TripBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TripBudget
        fields = ['ammount']

