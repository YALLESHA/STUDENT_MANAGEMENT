from django.db import models
from accounts.models import User

class Student(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'}
    )
    roll_no = models.CharField(max_length=20, unique=True)
    class_name = models.CharField(max_length=20)
    section = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user.username} ({self.roll_no})"
