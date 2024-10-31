from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from vp_users.models import User


class SaleCard(models.Model):
    title: models.CharField = models.CharField(max_length=100, db_index=True)
    price: models.CharField = models.CharField(max_length=100)
    description: models.CharField = models.CharField(max_length=500, null=True, blank=True)
    rating: models.FloatField = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True
    )
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published: models.BooleanField = models.BooleanField()

    def __str__(self):
        return self.title
