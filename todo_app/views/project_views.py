from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, TemplateView

from todo_app.forms import ProjectForm, ProjectTaskForm, \
    ManageUsersOnProjectForm, RemoveUserFromProjectForm
from todo_app.models import Project, Task


class AllProjectsView(ListView):
    template_name = "project/all_projects.html"
    context_object_name = "projects"
    model = Project


class ProjectView(DetailView):
    template_name = "project/detailed_project.html"
    model = Project


class ProjectCreateView(UserPassesTestMixin, CreateView):
    template_name = "project/project_create.html"
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("detailed_project", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.has_perm('todo_app.add_project')


class ProjectTaskCreateView(PermissionRequiredMixin, CreateView):
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

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        return self.request.user in project.users.all()



class AddUserToProjectView(PermissionRequiredMixin, TemplateView):
    template_name = "project/add_user_to_project.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = ManageUsersOnProjectForm()
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        context["project"] = project
        context["form"] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = ManageUsersOnProjectForm(request.POST)
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        context = self.get_context_data(**kwargs)
        context["project"] = project
        context["form"] = form
        if form.is_valid():
            user = form.cleaned_data.get("user")
            project.users.add(user)
            return redirect("detailed_project", pk=project.pk)
        return render(request, "project/add_user_to_project.html", context)

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        return self.request.user in project.users.all()




class RemoveUserFromProjectView(PermissionRequiredMixin, TemplateView):
    template_name = "project/remove_user_from_project.html"

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        context = self.get_context_data(**kwargs)
        users_on_project = project.users.all()
        form = RemoveUserFromProjectForm(initial={"user": users_on_project})
        context["users_on_project"] = users_on_project
        context["project"] = project
        context["form"] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = RemoveUserFromProjectForm(request.POST)
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        context = self.get_context_data(**kwargs)
        context["project"] = project
        context["form"] = form
        if form.is_valid():
            user = form.cleaned_data.get("user")
            project.users.remove(user)
            return redirect("detailed_project", pk=project.pk)
        return render(request, "project/remove_user_from_project.html", context)

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get("pk"))
        return self.request.user in project.users.all()


