from django.db import models

from common.models import BaseModel


class DrugQuerySet(models.QuerySet):
    def published(self):
        return self.filter(published=True)


class Drug(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    public = models.BooleanField(default=False, verbose_name="В продаже", db_index=True)

    objects = DrugQuerySet.as_manager()

    class Meta:
        verbose_name = "Препарат"
        verbose_name_plural = "Препараты"

    def __str__(self):
        return self.name
