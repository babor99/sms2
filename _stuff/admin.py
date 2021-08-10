from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Stuff)
class StuffAdmin(admin.ModelAdmin):
    list_display = ('user', 'image', 'age', 'stuff_id', 'phone', 'is_active', 'is_married')
    list_display_links = ('user',)
    list_filter = ('user', )
    search_fields = ('user', 'stuff_id')
    list_per_page = 10

@admin.register(StuffAttendance)
class StuffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('stuff', '_date', 'is_present')
    list_display_links = ('stuff', )
    list_filter = ('stuff',)
    search_fields = ('stuff', 'is_present')
    list_per_page = 10

