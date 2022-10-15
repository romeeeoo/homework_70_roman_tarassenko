from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from todo_app.forms import ProjectForm, ProjectTaskForm
from todo_app.models import Project, Task


class AllProjectsView(ListView):
    template_name = "project/all_projects.html"
    context_object_name = "projects"
    model = Project


class ProjectView(DetailView):
    template_name = "project/detailed_project.html"
    model = Project


class ProjectCreateView(CreateView):
    template_name = "project/project_create.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("detailed_project", kwargs={"pk": self.object.pk})


class ProjectTaskCreateView(CreateView):
    model = Task
    template_name = "project/add_task_to_project.html"
    form_class = ProjectTaskForm

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        task = form.save(commit=False)
        task.project = project
        task.save()
        return redirect("detailed_project", pk=project.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        context["project"] = project
        return context

