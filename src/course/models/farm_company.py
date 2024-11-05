from django.db import models

from common.models import BaseModel


class FarmCompany(BaseModel):
    name = models.CharField(max_length=255, verbose_name="Название")

    class Meta:
        verbose_name = "Фарм. компания"
        verbose_name_plural = "Фарм. компании"

    def __str__(self):
        return self.name
