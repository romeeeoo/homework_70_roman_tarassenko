from django import forms

from todo_app.models import TaskStatus, Task, Project


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["summary",
                  "description",
                  "status",
                  "types", ]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "specification",
            "start_date",
            "project_deadline",
        ]


class ProjectTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "summary",
            "description",
            "status",
            "types",
        ]
