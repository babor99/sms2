from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'age', 'teacher_id', 'phone', 'is_active', 'is_married')
    list_display_links = ('user',)
    list_filter = ('user', )
    search_fields = ('user', 'teacher_id')
    list_per_page = 10

@admin.register(TeacherAttendance)
class TeacherAttendanceAdmin(admin.ModelAdmin):
    list_display = ('teacher', '_date', 'is_present')
    list_display_links = ('teacher', )
    list_filter = ('teacher',)
    search_fields = ('teacher', 'is_present')
    list_per_page = 10
