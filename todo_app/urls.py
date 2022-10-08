from django.urls import path
from todo_app.views import update_view, delete_view, confirm_delete_view, IndexView, TaskView, AddTaskView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddTaskView.as_view(), name='add_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='detailed_task'),
    path('task/', IndexView.as_view(), name='task_no_pk'),
    path('task/<int:pk>/update/', update_view, name='update_task'),
    path('task/<int:pk>/delete', delete_view, name='delete_task'),
    path('task/<int:pk>/confirm-delete', confirm_delete_view, name='confirm_delete_task')
]
