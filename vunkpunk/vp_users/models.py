from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Dorm(models.TextChoices):
        PUNK = "punk", "ПУНК"
        VUNK = "vunk", "ВУНК"
        UNKNOWN = "unk", "Не указано"

    class Faculty(models.TextChoices):
        MATMEH = "matmeh", "Математико-Механический"
        PMPU = "pmpu", "Прикладной математики, процессов управдения"
        CHEMFAC = "chemfac", "Химический"
        PHYSFAC = "physfac", "Физический"
        UNKNOWN = "unk", "Не указан"

    surname: models.CharField = models.CharField(max_length=40, blank=True, default="не указано")
    patronymic: models.CharField = models.CharField(max_length=40, blank=True, default="не указано")
    dormitory: models.CharField = models.CharField(choices=Dorm, max_length=50, blank=True, default=Dorm.UNKNOWN)
    faculty: models.CharField = models.CharField(choices=Faculty, max_length=50, blank=True, default=Faculty.UNKNOWN)
    contact: models.CharField = models.CharField(max_length=255, blank=True, default="не указано")
    description: models.CharField = models.CharField(max_length=255, blank=True, default="не указано")

    def __str__(self) -> str:
        return self.username