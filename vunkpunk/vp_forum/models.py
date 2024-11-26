from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from vp_users.models import User


class SaleCard(models.Model):
    title: models.CharField = models.CharField(max_length=100, db_index=True)
    photo: models.ImageField = models.ImageField(
        upload_to="images_manager/image_folder/salecard/",
        default="images_manager/image_folder/default/salecard_default.jpg",
    )
    price: models.CharField = models.CharField(max_length=100)
    description: models.CharField = models.CharField(max_length=500, null=True, blank=True)
    dormitory: models.CharField = models.CharField(max_length=50, default="Не указано")
    rating: models.FloatField = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True
    )
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published: models.BooleanField = models.BooleanField()

    def __str__(self):
        return self.title
