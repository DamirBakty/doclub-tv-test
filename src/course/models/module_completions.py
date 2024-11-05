from django.db import models

from common.models import BaseModel, User
from .module import Module


class ModuleCompletion(BaseModel):
    video_started = models.BooleanField(default=False)
    file_downloaded = models.BooleanField(default=False)
    test_completed = models.BooleanField(default=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="module_completions",
        verbose_name="Пользователь",
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        related_name="module_completions",
        verbose_name="Модуль",
    )

    class Meta:
        verbose_name = "Прохождение модуля"
        verbose_name_plural = "Прохождения модулей"
        unique_together = (("user", "module"),)
