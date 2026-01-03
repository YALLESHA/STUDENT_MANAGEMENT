from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Attendance
from django.contrib.auth.decorators import login_required

@login_required
def attendance_list(request):
    """
    List all attendance records.
    Admin/Teacher sees all, students see only their own.
    """
    user = request.user

    if user.role == 'student':
        attendance = Attendance.objects.filter(student__user=user)
    else:
        attendance = Attendance.objects.all()

    context = {
        'attendance': attendance
    }
    return render(request, 'attendance.html', context)
