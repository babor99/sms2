from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from .models import *
from .serializers import *
from _school.permissions import CustomDjangoModelPermissions

# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomDjangoModelPermissions]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def list(self, request):
        queryset = Teacher.objects.all()
        serializer = TeacherSerializer(queryset, many=True, context={'request':request})

        return Response({'error':False, 'message':'Teacher data', 'data':serializer.data})


class TeacheAttendanceViewSet(viewsets.ModelViewSet):
    permission_classes = [CustomDjangoModelPermissions]
    queryset = TeacherAttendance.objects.all()
    serializer_class = TeacherAttendanceSerializer

    def list(self, request):
        queryset = TeacherAttendance.objects.all()
        serializer = TeacherAttendanceSerializer(queryset, many=True, context={'request':request})

        return Response({'error':False, 'message':'Teacher data', 'data':serializer.data})