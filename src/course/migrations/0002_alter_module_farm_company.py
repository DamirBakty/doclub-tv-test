# Generated by Django 5.1.2 on 2024-11-05 09:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="module",
            name="farm_company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="course.farmcompany",
                verbose_name="Фарм. компания",
            ),
        ),
    ]
