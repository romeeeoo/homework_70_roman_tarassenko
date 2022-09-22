from django.urls import path
from todo_app.views import index_view, add_view, detail_view

urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view),
    path('task/<int:pk>', detail_view, name='detailed_task'),
    path('task/', index_view)
]
