from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Marks

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks', 'date')
    list_filter = ('subject', 'date')
    search_fields = ('student__user__username', 'subject')
