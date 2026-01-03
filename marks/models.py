from django.db import models
from students.models import Student

class Marks(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='marks_records'
    )
    subject = models.CharField(max_length=50)
    marks = models.PositiveIntegerField()  # Only positive integers
    date = models.DateField(auto_now_add=True)  # Optional: track exam date

    class Meta:
        unique_together = ('student', 'subject', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.student} - {self.subject} : {self.marks}"
