from django.db import models
from tasks.models import Task

class Pomodoro(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    duration = models.IntegerField(default=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} - {self.duration} min"