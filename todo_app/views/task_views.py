from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView

from todo_app.forms import TaskForm, SimpleSearchForm
from todo_app.models import Task


class IndexView(ListView):
    template_name = "task/index.html"
    context_object_name = "tasks"
    model = Task
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class AddTaskView(LoginRequiredMixin, TemplateView):
    template_name = "task/add_new_task.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = TaskForm()
        context["form"] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save()
            return redirect("detailed_task", pk=task.pk)
        return render(request, "task/add_new_task.html", context={"form": form})


class TaskView(TemplateView):
    template_name = "task/detailed_task.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=kwargs["pk"])
        print(context)
        return context

# class UpdateTaskView(TemplateView):
#     template_name = "task/update_task.html"
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["task"] = get_object_or_404(Task, pk=kwargs["pk"])
#         return context
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         form = TaskForm(instance=context["task"])
#         context["form"] = form
#         return self.render_to_response(context)
#
#     def post(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs["pk"])
#         form = TaskForm(request.POST, instance=task)
#         if form.is_valid():
#             task = form.save()
#             return redirect("detailed_task", pk=task.pk)
#         return render(request, "task/add_new_task.html", context={"form": form})


# class CommentUpdateView(UpdateView):
#     model = Comment
#     template_name = 'comment/update.html'
#     form_class = ArticleCommentForm
#     context_object_name = 'comment'
#
#
#     def get_success_url(self):
#         return reverse('article_view', kwargs={'pk': self.object.article.pk})

class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task/update_task.html"
    form_class = TaskForm
    context_object_name = "task"

    def get_success_url(self):
        return reverse("detailed_project", kwargs={"pk": self.object.project.pk})


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    template_name = 'task/task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')
