from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('accounts.urls')),

    path('dashboard/', dashboard, name='dashboard'),
    path('attendance/', include('attendance.urls')),
    path('marks/', include('marks.urls')),
]
