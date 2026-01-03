from django.urls import path
from .views import attendance_list

urlpatterns = [
    path('', attendance_list, name='attendance_list'),
]
