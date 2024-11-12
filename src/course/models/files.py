from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from common.models import BaseModel


class File(BaseModel):
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE, related_name="files"
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    file = models.FileField(upload_to="files/%Y/%m/%d", verbose_name="Файл")

    class Meta:
        verbose_name = "Файл"
        verbose_name_plural = "Файлы"
