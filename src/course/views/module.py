from rest_framework import permissions, mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from course.models import Module, ModuleCompletion
from course.serializers import ModuleSerializer


class ModuleViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = (
        Module.objects.select_related("farm_company", "course")
        .prefetch_related("drugs", "timecodes", "files", "module_completions")
        .all()
    )
    serializer_class = ModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=None,
    )
    def watch_video(self, request, pk=None):
        user = request.user
        module_completion, _ = ModuleCompletion.objects.get_or_create(
            user=user,
            module_id=pk,
        )
        module_completion.video_started = True
        module_completion.save()
        return Response(data={"message": "Video started"}, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=None,
    )
    def download_file(self, request, pk=None):
        user = request.user
        module_completion, _ = ModuleCompletion.objects.get_or_create(
            user=user,
            module_id=pk,
        )
        module_completion.file_downloaded = True
        module_completion.save()
        return Response(data={"message": "Files downloaded"}, status=status.HTTP_200_OK)

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=None,
    )
    def complete_test(self, request, pk=None):
        user = request.user
        module_completion, _ = ModuleCompletion.objects.get_or_create(
            user=user,
            module_id=pk,
        )
        module_completion.test_completed = True
        module_completion.save()
        return Response(data={"message": "Test completed"}, status=status.HTTP_200_OK)
