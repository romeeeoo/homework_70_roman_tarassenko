from rest_framework import serializers

from todo_app.models import Project, Task, TaskStatus, TaskType


class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ("id", "name")
        read_only_fields = ("id",)


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ("id", "name")
        read_only_fields = ("id",)


class TaskSerializer(serializers.ModelSerializer):
    status = TaskStatusSerializer(read_only=True)
    types = TaskTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ("id",
                  "summary",
                  "description",
                  "status",
                  "types",)
        read_only_fields = (
            "id",)


# class ProjectSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200, required=True, allow_blank=False)
#     specification = serializers.CharField(max_length=1000, required=True, min_length=10, allow_blank=False)
#     start_date = serializers.DateField()
#     project_deadline = serializers.DateField()
#     tasks = TaskSerializer(many=True)
#
#     def create(self, validated_data):
#         return Project.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         for key, value in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()

class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ("id",
                  "name",
                  "specification",
                  "start_date",
                  "project_deadline",
                  "tasks"
                  )
        read_only_fields = (
            "id",)
