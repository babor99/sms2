from _teacher.views import TeacherViewSet
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('teacher', TeacherViewSet, basename='teachers' )
router.register('teacher_attendances', TeacheAttendanceViewSet, basename='teacher_attendances' )

urlpatterns = [
    path('', include(router.urls))
]
