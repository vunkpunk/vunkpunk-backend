# Generated by Django 5.1.2 on 2024-11-26 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vp_forum", "0004_alter_salecard_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="salecard",
            name="dormitory",
            field=models.CharField(default="Не указано", max_length=50),
        ),
    ]