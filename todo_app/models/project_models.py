from django.db import models
from todo_app.validators import min_length_validation


class Project(models.Model):
    name = models.CharField(max_length=200, validators=(min_length_validation,))
    specification = models.TextField(null=True, blank=True)
    start_date = models.DateField()
    project_deadline = models.DateField()
    users = models.ManyToManyField(to="auth.User", related_name="projects", blank=True)

    def __str__(self):
        return f"{self.pk}. {self.name}"
