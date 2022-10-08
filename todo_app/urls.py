from django.urls import path
from todo_app.views import IndexView, TaskView, AddTaskView, UpdateTaskView, DeleteTaskView, ConfirmDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='detailed_task'),
    path('task/', IndexView.as_view(), name='task_no_pk'),
    path('task/<int:pk>/update/', UpdateTaskView.as_view(), name='update_task'),
    path('task/<int:pk>/delete', DeleteTaskView.as_view(), name='delete_task'),
    path('task/<int:pk>/confirm-delete', ConfirmDeleteView.as_view(), name='confirm_delete_task')
]
