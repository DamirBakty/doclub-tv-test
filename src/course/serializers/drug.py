from rest_framework import serializers

from course.models import Drug


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = "__all__"
