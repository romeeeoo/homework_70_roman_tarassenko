from django.urls import path
from todo_app.views import index_view, add_view

urlpatterns = [
    path('', index_view, name="index_view"),
    path('add/', add_view)
]
