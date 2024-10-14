# Generated by Django 5.1.1 on 2024-10-14 17:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="banner",
            name="created_date",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="Created_date",
            ),
            preserve_default=False,
        ),
    ]
