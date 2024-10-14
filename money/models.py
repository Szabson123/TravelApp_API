from django.db import models


class TripBudget(models.Model):
    ammount = models.IntegerField()


class TripBudgetItemPlus(models.Model):
    trip = models.ForeignKey(TripBudget, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ammount = models.IntegerField()
    
    
class TripBudgetItemMinus(models.Model):
    trip = models.ForeignKey(TripBudget, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    ammount = models.IntegerField()