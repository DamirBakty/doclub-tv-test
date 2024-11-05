from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "image",
                    "get_image_preview",
                    "position",
                    "groups",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_active")
    search_fields = ("username", "first_name", "last_name", "email")
    filter_horizontal = ("groups", "user_permissions")

    readonly_fields = [
        "get_image_preview",
    ]

    def get_image_preview(self, obj):
        if not obj.image:
            return "выберите картинку"
        return format_html(
            '<img src="{url}" style="max-height: 200px;"/>', url=obj.image.url
        )

    get_image_preview.short_description = "превью"


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
