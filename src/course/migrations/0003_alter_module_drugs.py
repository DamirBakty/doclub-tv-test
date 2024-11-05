# Generated by Django 5.1.2 on 2024-11-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0002_alter_module_farm_company"),
    ]

    operations = [
        migrations.AlterField(
            model_name="module",
            name="drugs",
            field=models.ManyToManyField(
                blank=True,
                related_name="modules",
                to="course.drug",
                verbose_name="Препараты",
            ),
        ),
    ]
