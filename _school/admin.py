from django.contrib import admin
from django.contrib.admin.filters import ListFilter

from .models import *
# Register your models here.
@admin.register(AdminUser)
class AdminUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'image')
    list_display_links = ('user', 'image')

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'total_students', 'total_exams')
    list_display_links = ('name',)
    list_filter = ('year',)
    search_fields = ('name', 'year')
    list_per_page = 10

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_students', 'total_sections')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', '_class', 'total_students')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject_code', 'total_chapter')
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    list_per_page = 10

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'father_name', 'mother_name', 'age', 'student_id', '_class', 'section', '_group', )
    list_display_links = ('user', 'image')
    list_filter = ('user', '_class')
    search_fields = ('name', '_class')
    list_per_page = 10

@admin.register(StudentAttendance)
class StudentAttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', '_date', 'is_present')
    list_display_links = ('student',)
    list_filter = ('student',)
    search_fields = ('student', '_date')
    list_per_page = 10

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'term', 'total_mark', 'grade', 'is_passed')
    list_display_links = ('student', 'subject')
    list_filter = ('student', 'term')
    search_fields = ('student', 'term')
    list_per_page = 10

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('subject', '_class', 'term', 'is_completed', 'duration', '_date')
    list_display_links = ('subject', '_class')
    list_filter = ('subject', '_class')
    search_fields = ('subject', '_class')
    list_per_page = 10

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'stuff', 'month', 'salary_amount', 'paying_date')
    list_display_links = ('teacher', 'stuff')
    list_filter = ('teacher', 'stuff')
    search_fields = ('teacher', 'stuff')
    list_per_page = 10

@admin.register(LogisticsExpenditure)
class LogisticsExpenditureAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'receipt_no', 'model_no', 'company')
    list_display_links = ('name',)
    list_filter = ('name', 'amount')
    search_fields = ('name', 'amount')
    list_per_page = 10


