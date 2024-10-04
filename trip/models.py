from django.db import models
from user.models import CustomUser


class Item(models.Model):
    name = models.CharField(max_length=255)
    packed = models.BooleanField(default=False)
    

class NeededList(models.Model):
    name = models.CharField(max_length=255)
    item = models.ManyToManyField(Item, null=True, blank=True, related_name="items")


class Trip(models.Model):
    name = models.CharField(max_length=255)
    item_list = models.ManyToManyField(NeededList, null=True, blank=True)
    

