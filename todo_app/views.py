from django.shortcuts import render, redirect, get_object_or_404

from todo_app.forms import TaskForm
from todo_app.models import Task


# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add_view(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'add_new_task.html', context={'form': form})
    elif request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                description=form.cleaned_data['description'],
                detailed_description=form.cleaned_data['detailed_description'],
                status=form.cleaned_data['status'],
                deadline=form.cleaned_data['deadline']
            )
            return redirect("detailed_task", pk=new_task.pk)
        else:
            return render(request, 'add_new_task.html', context={'form': form})


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detailed_task.html', context={'task': task})
