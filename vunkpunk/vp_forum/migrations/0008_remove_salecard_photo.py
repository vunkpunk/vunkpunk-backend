# Generated by Django 5.1.4 on 2024-12-17 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vp_forum", "0007_alter_salecard_time_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salecard",
            name="photo",
        ),
    ]
