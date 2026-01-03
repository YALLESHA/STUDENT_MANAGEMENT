from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Marks
from django.contrib.auth.decorators import login_required

@login_required
def marks_list(request):
    """
    List all marks.
    Admin/Teacher sees all, students see only their own.
    """
    user = request.user

    if user.role == 'student':
        marks = Marks.objects.filter(student__user=user)
    else:
        marks = Marks.objects.all()

    context = {
        'marks': marks
    }
    return render(request, 'marks.html', context)
