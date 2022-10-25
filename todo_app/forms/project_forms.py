from django import forms
from django.contrib.auth.models import User

from todo_app.models import Project, Task


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
    # status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), initial=TaskStatus.objects.filter(name="new"))

    class Meta:
        model = Task
        fields = [
            "summary",
            "description",
            "status",
            "types",
        ]


# class AddUserToProjectForm(forms.ModelForm):
#     username = forms.ModelChoiceField(queryset=User.objects.all())
#
#     class Meta:
#         model = User
#         fields = ["username"]

class ManageUsersOnProjectForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())


class RemoveUserFromProjectForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())