# Generated by Django 5.1.2 on 2024-11-05 10:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0004_alter_module_speakers"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="file",
            options={"verbose_name": "Файл", "verbose_name_plural": "Файлы"},
        ),
    ]
