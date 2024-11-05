from rest_framework import permissions, mixins
from rest_framework.viewsets import GenericViewSet

from course.models import Course
from course.serializers import CourseSerializer


class CourseViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.prefetch_related("drugs", "lecturers").all()
    permission_classes = (permissions.AllowAny,)
