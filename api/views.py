from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import ProjectSerializer
from todo_app.models import Project


class ProjectSimpleView(View):
    def get(self, request, *args, **kwargs):
        objects = Project.objects.all()
        serializer = ProjectSerializer(objects, many=True)
        return JsonResponse(serializer.data)


class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get("pk"))
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdateView(APIView):
    def put(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=kwargs.get("pk"))
        serializer = ProjectSerializer(project, data=request.data)
        print(request.data)
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


