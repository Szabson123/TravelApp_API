from django.db import models
from user.models import CustomUser


class ItemList(models.Model):
    name = models.CharField(max_length=255)
    packed = models.BooleanField(default=False)
    

class NeededList(models.Model):
    name = models.CharField(max_length=255)
    item = models.ManyToManyField(ItemList, null=True, blank=True)


class Trip(models.Model):
    name = models.CharField(max_length=255)
    item_list = models.ManyToManyField(NeededList, null=True, blank=True)
    

