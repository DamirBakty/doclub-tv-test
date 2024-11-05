from rest_framework import serializers

from course.models import ModuleCompletion


class ModuleCompletionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleCompletion
        fields = ("video_started", "file_downloaded", "test_completed")
