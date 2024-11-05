from django.db import models

from common.models import BaseModel, User
from .module_completions import ModuleCompletion


class Certificate(BaseModel):
    user = models.ForeignKey(
        User,
        related_name="certificates",
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
    )
    module_completion = models.OneToOneField(
        ModuleCompletion,
        related_name="certificate",
        on_delete=models.CASCADE,
        verbose_name="Прохождение модуля",
    )

    class Meta:
        verbose_name = "Сертификат"
        verbose_name_plural = "Сертификаты"
        unique_together = (("user", "module_completion"),)
