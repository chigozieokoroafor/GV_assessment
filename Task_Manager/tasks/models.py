from django.db import models

# Create your models here.
class StatusChoices(models.TextChoices):
    pending = "pending"
    completed = "completed"

class Task(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    due_date = models.DateTimeField()
    status = models.TextField(max_length = 10, choices=StatusChoices.choices)
    # user = models.ForeignKey(User)


