from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.shortcuts import get_object_or_404


class UserManager(BaseUserManager):
    @staticmethod
    def get_user(data):
        return get_object_or_404(User, **data)

    def create_user(self, password: str = None, **kwargs) -> "User":
        user = self.model(**kwargs, is_active=False)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, password: str = None, **kwargs) -> "User":
        user = self.model(is_active=True, is_staff=True, is_superuser=True, **kwargs)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    image = models.ImageField(
        upload_to="users", verbose_name="Фото", null=True, blank=True
    )
    position = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Должность"
    )

    objects = UserManager()

    class Meta:
        db_table = "auth_user"

    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
