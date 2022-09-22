from django.shortcuts import render, redirect, get_object_or_404

from todo_app.models import Task


# Create your views here.
def index_view(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'index.html', context)


def add_view(request):
    if request.method == 'GET':
        return render(request, 'add_new_task.html')
    elif request.method == 'POST':
        task_data = {'description': request.POST.get('description'),
                     'status': request.POST.get('status'),
                     # 'deadline': request.POST.get('deadline'),
                     'detailed_description': request.POST.get('detailed_description')
                     }
        new_task = Task.objects.create(**task_data)
        return redirect("detailed_task", pk=new_task.pk)


def detail_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'detailed_task.html', context={'task': task})
