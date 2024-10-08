from django.urls import path, include
from .views import ItemListViewSet, TripViewSet, NeededListViewSet

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'my_trips', TripViewSet, basename='trips')
router.register(r'neededlist/(?P<needed_list_pk>\d+)/items', ItemListViewSet, basename='itemlist')
router.register(r'my_lists', NeededListViewSet, basename='required_fields')

urlpatterns = [
    path('', include(router.urls))
]
