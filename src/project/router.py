from rest_framework import routers
from course.views import CourseViewSet, ModuleViewSet

router = routers.DefaultRouter()

router.register(r"modules", ModuleViewSet, basename="modules")

router.register(r"courses", CourseViewSet, basename="courses")
