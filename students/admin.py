from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'roll_no', 'class_name', 'section')
    search_fields = ('user__username', 'roll_no')
    list_filter = ('class_name', 'section')
