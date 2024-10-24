from django.db import models
from user.models import CustomUser
from money.models import TripBudget
import pycountry


COUNTRIES = [('None', 'None')] + [(country.name, country.name) for country in pycountry.countries]


class Item(models.Model):
    name = models.CharField(max_length=255)
    packed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.name
    

class NeededList(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField(Item, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    
    def __str__(self) -> str:
        return self.name


class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    country = models.CharField(choices=COUNTRIES, default=None, max_length=255, blank=True)
    item_list = models.ForeignKey(NeededList, on_delete=models.CASCADE, blank=True, null=True)
    budget = models.OneToOneField(TripBudget, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    

