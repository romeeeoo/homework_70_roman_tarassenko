from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer, TaskSerializer
from todo_app.models import Project, Task


class ProjectSimpleView(View):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)
        return JsonResponse(serializer.data, safe=False)


class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get("pk"))
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get("pk"))
        serializer = ProjectSerializer(data=request.data, instance=project)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class TaskUpdateView(UpdateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class TaskUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get("pk"))
        serializer = TaskSerializer(data=request.data, instance=task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteProjectView(APIView):
    def delete (self, *args, **kwargs):
        pk = kwargs.get("pk")
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response(pk, status=status.HTTP_200_OK)

class DeleteTaskView(APIView):
    def delete (self, *args, **kwargs):
        pk = kwargs.get("pk")
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(pk, status=status.HTTP_200_OK)



