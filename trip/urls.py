from django.urls import path, include
from .views import ItemListViewSet
from rest_framework import routers

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'neededlist/(?P<needed_list_pk>\d+)/items', ItemListViewSet, basename='itemlist')

urlpatterns = [
    path('', include(router.urls))
]