from django.urls import path
from todo_app.views import index_view, add_view, detail_view, update_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='add_task'),
    path('task/<int:pk>/', detail_view, name='detailed_task'),
    path('task/', index_view, name='task_no_pk'),
    path('task/<int:pk>/update/', update_view, name='update_task')
]
