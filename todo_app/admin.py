from django.contrib import admin

from todo_app.models import Task, TaskStatus, TaskType

# Register your models here.
admin.site.register(Task)
admin.site.register(TaskStatus)
admin.site.register(TaskType)
