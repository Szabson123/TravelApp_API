from django.urls import path, include
from .views import ItemListViewSet, TripViewSet
from rest_framework import routers

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('(?P<trip_pk>\d+)/(?P<needed_list_pk>\d+)', ItemListViewSet, basename='itemlist')
router.register('my_trips', TripViewSet, basename='trips')

urlpatterns = [
    path('', include(router.urls))
]