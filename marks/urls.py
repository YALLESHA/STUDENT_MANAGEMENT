from django.urls import path
from .views import marks_list

urlpatterns = [
    path('', marks_list, name='marks_list'),
]
