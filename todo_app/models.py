from django.db import models

from todo_app.validators import min_length_validation, max_length_validation


# Create your models here.
class TaskStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class TaskType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    summary = models.CharField(max_length=200, validators=(min_length_validation,))
    description = models.TextField(null=True, blank=True, validators=(min_length_validation, max_length_validation))
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    types = models.ManyToManyField(to="todo_app.TaskType", related_name="tasks", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.pk, self.summary)

