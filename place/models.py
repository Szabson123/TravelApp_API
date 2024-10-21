from django.db import models
from trip.models import Trip
from user.models import CustomUser


class Route(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    trip = models.ForeignKey(Trip, models.CASCADE, related_name='routes')
    description = models.TextField()


class Place(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    route = models.ForeignKey(Route, on_delete=models.CASCADE, null=True, blank=True)
    

    
    



