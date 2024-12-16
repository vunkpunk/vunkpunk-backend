# Generated by Django 5.1.2 on 2024-11-27 13:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vp_forum", "0006_salecard_contact_salecard_time_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salecard",
            name="time_created",
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
