from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from todo_app.forms import ProjectForm
from todo_app.models import Project


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
