from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    todo_name = models.CharField(max_length=500, unique=True)
    only_admin = models.BooleanField(default=False)
    def __str__(self):
        return self.todo_name

class Task_category(models.Model):
    category_name = models.CharField(max_length=500)
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name

p_choices = (
    ("critical", "critical"),
    ("high", "high"),
    ("neutral", "neutral"),
    ("low", "low"),
)

class Todo_data(models.Model):
    task = models.CharField(max_length=500)
    task_type = models.ForeignKey(Task_category, on_delete = models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete = models.CASCADE) 
    priority = models.CharField(max_length=100, choices=p_choices)
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete = models.CASCADE)
    deadline = models.DateField()

    def __str__(self):
        return self.task[:50]

