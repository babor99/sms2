from django.core import exceptions
from django.shortcuts import render
import json
from django.contrib import auth
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import jwt

from .models import *
from .serializers import *
from .permissions import CustomDjangoModelPermissions

# Create your views here.
class CustomTokenObtainView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        data = request.data
        if not data:
            return Response({'error': True, 'message': 'No data provided'})
        username = data['username']
        password = data['password']
        user_type = str(data['user_type'])
        print(user_type)

        user = auth.authenticate(username=username, password=password)
        user_types = {'1':'Admin', '2':'Student', '3':'Teacher', '4':'Stuff'}
        user_dict = {}
        user_group = UserSerializer(user).data
        for key, value in user_group.items():
            user_dict[key] = value

        if user:
            if str(user_type) == str(user_dict['groups'][0]):
                auth_token = jwt.encode({'username':user.username}, settings.JWT_SECRET_KEY, algorithm="HS256")
                serializer = UserSerializer(user)
                data = {'error':False,'user':serializer.data, 'token':auth_token}
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({'error':True, 'message':f"You can't login as {user_types[user_type]}"})    
        return Response({'error':True,'message':'Invalid credentials given.'})


class TermViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Term.objects.all()
    serializer_class = TermSerializer

    def list(self, request):
        queryset = Term.objects.all()
        serializer = TermSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Term data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch term data."})
    
    def retrieve(self, request, pk=None):
        queryset = Term.objects.get(id=pk)
        serializer = TermSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Term data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single term data."})

    def create(self, request):
        data = request.data
        try:
            serializer = TermSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Term data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving term data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Term.objects.get(id=pk)
            serializer = TermSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Term data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update term data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Term.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Term data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete term data."} 
        return Response(res)


class ClassViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

    def list(self, request):
        queryset = Class.objects.all()
        serializer = ClassSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message': 'Success! Class data fetched successfully.', 'data':serializer.data})
        else:
            return Response({'error':True, 'message': "Failed! Can't fetch class data."})

    def retrieve(self, request, pk=None):
        queryset = Class.objects.get(id=pk)
        serializer = ClassSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Class data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fecth single class data."})

    def create(self, request):
        data = request.data
        try:
            serializer = ClassSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Class data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving class data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Class.objects.get(id=pk)
            serializer = ClassSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Class data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update class data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Class.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Class data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete class data."} 
        return Response(res)
            

class SectionViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

    def list(self, request):
        queryset = Section.objects.all()
        serializer = SectionSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Section data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch section data."})
    
    def retrieve(self, request, pk=None):
        queryset = Section.objects.get(id=pk)
        serializer = SectionSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Section data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single section data."})

    def create(self, request):
        data = request.data
        try:
            serializer = SectionSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Section data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving section data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Section.objects.get(id=pk)
            serializer = SectionSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Section data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update section data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Section.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Section data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete section data."} 
        return Response(res)


class SubjectViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request):
        queryset = Subject.objects.all()
        serializer = SubjectSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Subject data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch subject data."})
    
    def retrieve(self, request, pk=None):
        queryset = Subject.objects.get(id=pk)
        serializer = SubjectSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Subject data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single subject data."})

    def create(self, request):
        data = request.data
        try:
            serializer = SubjectSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Subject data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving subject data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Subject.objects.get(id=pk)
            serializer = SubjectSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Subject data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update subject data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Subject.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Subject data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete subject data."} 
        return Response(res)


class StudentViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Student data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch Student data."})
    
    def retrieve(self, request, pk=None):
        queryset = Student.objects.get(id=pk)
        serializer = StudentSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Student data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single Student data."})

    def create(self, request):
        data = request.data
        try:
            serializer = StudentSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Student data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving Student data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Student.objects.get(id=pk)
            serializer = StudentSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Student data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update Student data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Student.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Student data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete Student data."} 
        return Response(res)


class StudentAttendanceViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = StudentAttendance.objects.all()
    serializer_class = StudentAttendanceSerializer

    def list(self, request):
        queryset = StudentAttendance.objects.all()
        serializer = StudentAttendanceSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! StudentAttendance data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch StudentAttendance data."})
    
    def retrieve(self, request, pk=None):
        queryset = StudentAttendance.objects.get(id=pk)
        serializer = StudentAttendanceSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! StudentAttendance data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single StudentAttendance data."})

    def create(self, request):
        data = request.data
        try:
            serializer = StudentAttendanceSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! StudentAttendance data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving StudentAttendance data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = StudentAttendance.objects.get(id=pk)
            serializer = StudentAttendanceSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! StudentAttendance data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update StudentAttendance data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = StudentAttendance.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! StudentAttendance data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete StudentAttendance data."} 
        return Response(res)


class ResultViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def list(self, request):
        queryset = Result.objects.all()
        serializer = ResultSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Result data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch Result data."})
    
    def retrieve(self, request, pk=None):
        queryset = Result.objects.get(id=pk)
        serializer = ResultSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Result data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single Result data."})

    def create(self, request):
        data = request.data
        try:
            serializer = ResultSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Result data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving Result data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Result.objects.get(id=pk)
            serializer = ResultSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Result data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update Result data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Result.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Result data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete Result data."} 
        return Response(res)


class ExamViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    
    def list(self, request):
        queryset = Exam.objects.all()
        serializer = ExamSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Exam data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch Exam data."})
    
    def retrieve(self, request, pk=None):
        queryset = Exam.objects.get(id=pk)
        serializer = ExamSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Exam data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single Exam data."})

    def create(self, request):
        data = request.data
        try:
            serializer = ExamSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Exam data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving Exam data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Exam.objects.get(id=pk)
            serializer = ExamSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Exam data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update Exam data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Exam.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Exam data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete Exam data."} 
        return Response(res)


class SalaryViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer

    def list(self, request):
        queryset = Salary.objects.all()
        serializer = SalarySerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Salary data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch Salary data."})
    
    def retrieve(self, request, pk=None):
        queryset = Salary.objects.get(id=pk)
        serializer = SalarySerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! Salary data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single Salary data."})

    def create(self, request):
        data = request.data
        try:
            serializer = SalarySerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! Salary data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving Salary data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = Salary.objects.get(id=pk)
            serializer = SalarySerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! Salary data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update Salary data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = Salary.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! Salary data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete Salary data."} 
        return Response(res)

    
class LogisticsExpenditureViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, CustomDjangoModelPermissions]
    queryset = LogisticsExpenditure.objects.all()
    serializer_class = LogisticsExpenditureSerializer

    def list(self, request):
        queryset = LogisticsExpenditure.objects.all()
        serializer = LogisticsExpendituretSerializer(queryset, many=True, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! LogisticsExpenditure data fetched successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Can't fetch LogisticsExpenditure data."})
    
    def retrieve(self, request, pk=None):
        queryset = LogisticsExpenditure.objects.get(id=pk)
        serializer = LogisticsExpenditureSerializer(queryset, context={'request':request})
        if request.user.is_authenticated:
            return Response({'error':False, 'message':"Success! LogisticsExpenditure data retrieved successfully.", 'data':serializer.data})
        else:
            return Response({'error':True, 'message':"Failed! Cann't fecth single LogisticsExpenditure data."})

    def create(self, request):
        data = request.data
        try:
            serializer = LogisticsExpenditureSerializer(data=data, context={'request':request})
            serializer.is_valid()
            if request.user.is_authenticated:
                serializer.save()
            res = {'error':False, 'message':'Success! LogisticsExpenditure data saved successfully.'}
        except:
            res = {'error':True, 'message':'Failed! Error during saving LogisticsExpenditure data.'}
        return Response(res)
    
    def update(self, request, pk=None):
        try:
            data = request.data
            queryset = LogisticsExpenditure.objects.get(id=pk)
            serializer = LogisticsExpenditureSerializer(queryset, data=data, context={'request':request})
            serializer.is_valid()
            serializer.save()
            res = {'error':False, 'message':'Success! LogisticsExpenditure data updated successfully.'}
        except:
            res = {'error':True, 'message':"Failed! Can't update LogisticsExpenditure data."}
        return Response(res)

    def destroy(self, request, pk=None):
        class_obj = LogisticsExpenditure.objects.get(id=pk)
        print('id ', pk)
        if request.user.is_authenticated:
            class_obj.delete()
            res = {'error':False, 'message':'Success! LogisticsExpenditure data has been deleted.'}
        else:
            res = {'error':True, 'message':"Failed! Can't delete LogisticsExpenditure data."} 
        return Response(res)