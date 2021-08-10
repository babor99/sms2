from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('terms', TermViewset, basename='terms')
router.register('classes', ClassViewset, basename='classes')
router.register('sections', SectionViewset, basename='sections')
router.register('subjects', SubjectViewset, basename='subjects')
router.register('students', StudentViewset, basename='students')
router.register('student_attendances', StudentAttendanceViewset, basename='student_attendances')
router.register('results', ResultViewset, basename='result')
router.register('exams', ExamViewset, basename='exam')
router.register('salaries', SalaryViewset, basename='salary')
router.register('logistics_expenditures', LogisticsExpenditureViewset, basename='logistics_expenditures')

urlpatterns = [
    path('', include(router.urls)),
    # path('terms/', TermViewset.as_view(), name='terms'),
]
