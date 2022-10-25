from django import forms

from todo_app.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        # status = forms.ModelChoiceField(queryset=TaskStatus.objects.all(), initial=TaskStatus.objects.first())

        model = Task
        fields = ["summary",
                  "description",
                  "status",
                  "types", ]


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Find")




