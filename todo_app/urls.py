from django.urls import path
from todo_app.views import index_view

urlpatterns = [
    path('', index_view)
]
