from django.urls import path, include
from .views import TripViewSet, NeededListViewSet

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'trips', TripViewSet, basename='trips')
router.register(r'my_lists', NeededListViewSet, basename='required_fields')

urlpatterns = [
    path('', include(router.urls))
]
