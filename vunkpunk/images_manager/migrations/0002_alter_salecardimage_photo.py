# Generated by Django 5.1.4 on 2024-12-17 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("images_manager", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="salecardimage",
            name="photo",
            field=models.ImageField(upload_to="images_manager/image_folder/salecard/"),
        ),
    ]
