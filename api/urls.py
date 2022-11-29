from django.urls import path

from api.views import ProjectDetailView, ProjectUpdateView, DeleteProjectView, ProjectSimpleView, TaskUpdateView, \
    TaskDetailView, DeleteTaskView

urlpatterns = [
    path('projects/', ProjectSimpleView.as_view(), name='projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detailed'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='tasks_detailed'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path("project/<int:pk>/delete/", DeleteProjectView.as_view(), name='project_delete'),
    path("task/<int:pk>/delete/", DeleteTaskView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='tasks_update'),
]
