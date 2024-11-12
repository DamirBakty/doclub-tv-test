from django.contrib.contenttypes.fields import GenericRelation
from django.db import models
from .files import File
from common.models import BaseModel, User
from .course import Course
from .drug import Drug
from .farm_company import FarmCompany


class Module(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="modules",
        verbose_name="Курс",
    )
    image = models.ImageField(upload_to="module/images", verbose_name="Фото")
    video = models.FileField(upload_to="module/videos", verbose_name="Видео")
    speakers = models.ManyToManyField(to=User, related_name="modules", blank=True)
    drugs = models.ManyToManyField(
        to=Drug, related_name="modules", verbose_name="Препараты", blank=True
    )
    farm_company = models.ForeignKey(
        to=FarmCompany,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Фарм. компания",
        blank=True,
    )
    disclaimer = models.TextField(verbose_name="Дисклеймер")
    files = GenericRelation(File, related_query_name="module")

    class Meta:
        verbose_name = "Модуль"
        verbose_name_plural = "Модули"

    def __str__(self):
        return self.name


class TimeCode(BaseModel):
    module = models.ForeignKey(
        Module,
        on_delete=models.CASCADE,
        verbose_name="Модуль",
        related_name="timecodes",
    )
    time = models.DurationField(verbose_name="Время")
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Тайм код"
        verbose_name_plural = "Тайм коды"
