from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class StatusChoices(models.TextChoices):
    pending = "pending"
    completed = "completed"

class Task(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField()
    status = models.CharField(max_length=15, choices=StatusChoices.choices, default = "pending" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ["-status", "-due_date"]


