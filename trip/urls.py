from django.urls import path, include
from .views import ItemListViewSet
from rest_framework import routers

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('(?P<trip_pk>\d+)/(?P<needed_list_pk>\d+)', ItemListViewSet, basename='itemlist')

urlpatterns = [
    path('', include(router.urls))
]