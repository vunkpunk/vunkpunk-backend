from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from vp_users.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=True).order_by("-time_created")


class Category(models.Model):
    name: models.CharField = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name


class SaleCard(models.Model):
    objects = models.Manager()
    published = PublishedManager()

    title: models.CharField = models.CharField(max_length=100, db_index=True)
    price: models.CharField = models.CharField(max_length=100)
    description: models.CharField = models.CharField(max_length=500, null=True, blank=True)
    contact: models.CharField = models.CharField(max_length=100, null=True, default="Не указано")
    dormitory: models.CharField = models.CharField(max_length=50, default="Не указано")
    rating: models.FloatField = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], null=True, blank=True
    )
    categories: models.ManyToManyField = models.ManyToManyField(Category, related_name="salecards", blank=True)
    time_created: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published: models.BooleanField = models.BooleanField()

    def __str__(self):
        return self.title
