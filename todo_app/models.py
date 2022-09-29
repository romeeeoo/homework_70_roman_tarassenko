from django.db import models


# Create your models here.
class TaskStatus(models.Model):
    status = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return "{}".format(self.status)


class Task(models.Model):
    description = models.CharField(max_length=200, null=False, blank=False)
    deadline = models.DateField(null=True, blank=True)
    detailed_description = models.TextField(null=True, blank=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.CASCADE)

    def __str__(self):
        return "{}. {}".format(self.pk, self.description, self.status)


