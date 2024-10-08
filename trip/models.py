from django.db import models
from user.models import CustomUser


class Item(models.Model):
    name = models.CharField(max_length=255)
    packed = models.BooleanField(default=False)
    

class NeededList(models.Model):
    name = models.CharField(max_length=255)
    item = models.ManyToManyField(Item, null=True, blank=True)


class Trip(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    item_list = models.ManyToManyField(NeededList, blank=True)
    

