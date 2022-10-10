from django import forms

from todo_app.models import TaskStatus, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["summary",
                  "description",
                  "status",
                  "types", ]

