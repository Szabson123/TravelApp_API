from django.urls import path, include
from .views import RouteViewSet 

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register(r'(?P<trip_id>\d+)/routes', RouteViewSet, basename='trip-routes')
router.register(r'(?P<route_id>\d+)/places', RouteViewSet, basename='places')

urlpatterns = [
    path('', include(router.urls))
]
