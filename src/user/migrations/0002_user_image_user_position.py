# Generated by Django 5.1.2 on 2024-11-05 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="users", verbose_name="Фото"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="position",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Должность"
            ),
        ),
    ]
