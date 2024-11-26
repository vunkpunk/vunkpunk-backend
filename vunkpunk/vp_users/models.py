from django.contrib.auth.models import AbstractUser
from django.db import models
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


class User(AbstractUser):
    class Dorm(models.TextChoices):
        PUNK = "punk", "ПУНК"
        VUNK = "vunk", "ВУНК"
        UNKNOWN = "unk", "Не указано"

    class Faculty(models.TextChoices):
        MATMEH = "matmeh", "Математико-Механический"
        PMPU = "pmpu", "Прикладной математики, процессов управления"
        CHEMFAC = "chemfac", "Химический"
        PHYSFAC = "physfac", "Физический"
        UNKNOWN = "unk", "Не указан"

    dormitory: models.CharField = models.CharField(choices=Dorm, max_length=50, blank=True, default=Dorm.UNKNOWN)
    faculty: models.CharField = models.CharField(choices=Faculty, max_length=50, blank=True, default=Faculty.UNKNOWN)
    contact: models.CharField = models.CharField(max_length=255, blank=True, default="не указано")
    description: models.CharField = models.CharField(max_length=255, blank=True, default="не указано")
    photo: models.ImageField = models.ImageField(
        upload_to="images_manager/image_folder/user/", default="images_manager/image_folder/default/user_default.jpg"
    )

    def __str__(self) -> str:
        return self.username
