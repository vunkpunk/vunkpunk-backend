# Generated by Django 5.1.2 on 2024-11-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vp_forum", "0005_salecard_dormitory"),
    ]

    operations = [
        migrations.AddField(
            model_name="salecard",
            name="contact",
            field=models.CharField(default="Не указано", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="salecard",
            name="time_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]