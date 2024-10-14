from django.urls import path, include
from .views import TripBudgetViewSet

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'trips', TripBudgetViewSet, basename='trips')

urlpatterns = [
    path('', include(router.urls))
]