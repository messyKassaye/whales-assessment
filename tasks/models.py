from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default='medium')
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
