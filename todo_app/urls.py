from django.urls import path
from todo_app.views import IndexView, TaskView, AddTaskView, UpdateTaskView, DeleteTaskView, \
    AllProjectsView, ProjectView, ProjectCreateView, ProjectTaskCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('add/', AddTaskView.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='detailed_task'),
    path('task/', IndexView.as_view(), name='task_no_pk'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<int:pk>/confirm-delete', DeleteTaskView.as_view(), name='confirm_delete_task'),
    path('project/', AllProjectsView.as_view(), name='all_projects'),
    path('project/<int:pk>/', ProjectView.as_view(), name='detailed_project'),
    path('project/add/', ProjectCreateView.as_view(), name='add_project'),
    path('project/<int:pk>/tasks/add', ProjectTaskCreateView.as_view(), name='add_project_task'),
]
