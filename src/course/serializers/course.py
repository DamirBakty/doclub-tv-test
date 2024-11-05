from rest_framework import serializers

from course.models import Course
from .drug import DrugSerializer
from user.serializers import UserSerializer


class CourseSerializer(serializers.ModelSerializer):
    lecturers = UserSerializer(many=True, read_only=True)
    drugs = DrugSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
