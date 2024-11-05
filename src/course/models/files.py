from common.models import BaseModel
from django.db import models
from .course import Course
from .module import Module


class File(BaseModel):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Курс",
        related_name="files",
    )
    module = models.ForeignKey(
        Module,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Модуль",
        related_name="files",
    )
    file = models.FileField(upload_to="files/%Y/%m/%d", verbose_name="Файл")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
