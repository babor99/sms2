from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('stuff', StuffViewSet, basename='stuff')
router.register('stuff_attendances', StuffAttendanceViewSet, basename='stuff_attendances')

urlpatterns = [
    path('', include(router.urls)),
]
