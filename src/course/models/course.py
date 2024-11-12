from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from common.models import BaseModel, User
from .drug import Drug
from .files import File


class Course(BaseModel):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to="course", verbose_name="Фото")
    lecturers = models.ManyToManyField(
        to=User, related_name="courses", verbose_name="Лекторы", blank=True
    )
    drugs = models.ManyToManyField(
        to=Drug, related_name="courses", verbose_name="Препараты", blank=True
    )
    disclaimer = models.TextField(verbose_name="Дисклеймер")
    files = GenericRelation(File, related_query_name="course")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name
