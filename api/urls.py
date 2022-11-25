from django.urls import path

from api.views import ProjectDetailView, ProjectUpdateView, DeleteProjectView

urlpatterns = [
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detailed'),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path("project/<int:pk>/delete/", DeleteProjectView.as_view(), name='project_delete')
]
