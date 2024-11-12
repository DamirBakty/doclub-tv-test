from django.contrib import admin
from django.utils.html import format_html
from django.contrib.contenttypes.admin import GenericTabularInline

from course.models import (
    Course,
    Module,
    File,
    ModuleCompletion,
    Drug,
    FarmCompany,
    Certificate,
)


class ModuleCompletionInline(admin.TabularInline):
    model = ModuleCompletion
    extra = 1


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 0


class FileInline(GenericTabularInline):
    model = File
    extra = 0


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_per_page = 20


@admin.register(FarmCompany)
class FarmCompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_per_page = 20


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_per_page = 20
    inlines = [FileInline, ModuleInline]
    fieldsets = (
        (
            "Общее",
            {
                "fields": [
                    "name",
                    "image",
                    "get_image_preview",
                ]
            },
        ),
        (
            "Подробно",
            {
                "fields": [
                    "description",
                    "drugs",
                    "disclaimer",
                ],
            },
        ),
    )

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


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    search_fields = ["name"]
    list_per_page = 20
    inlines = [
        FileInline,
        ModuleCompletionInline,
    ]

    autocomplete_fields = ["course", "farm_company"]
    fieldsets = (
        (
            "Общее",
            {
                "fields": [
                    "name",
                    "image",
                    "get_image_preview",
                    "video",
                ]
            },
        ),
        (
            "Подробно",
            {
                "fields": [
                    "course",
                    "farm_company",
                    "description",
                    "speakers",
                    "drugs",
                    "disclaimer",
                ],
            },
        ),
    )

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


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass


@admin.register(ModuleCompletion)
class ModuleCompletionAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user"]
