from _stuff.serializers import StuffSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from _school.permissions import CustomDjangoModelPermissions

from .models import *
from .serializers import *

# Create your views here.
class StuffViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomDjangoModelPermissions]
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

    def list(self, request):
        queryset = Stuff.objects.all()
        serializer = StuffSerializer(queryset, many=True, context={'request':request})

        return Response({'error':False, 'message':'Stuff data', 'data':serializer.data})


class StuffAttendanceViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomDjangoModelPermissions]
    queryset = StuffAttendance.objects.all()
    serializer_class = StuffAttendanceSerializer

    def list(self, request):
        queryset = StuffAttendance.objects.all()
        serializer = StuffAttendanceSerializer(queryset, many=True, context={'request':request})

        return Response({'error':False, 'message':'Stuff Attendance data', 'data':serializer.data})