from django.db import models
from vp_forum.models import SaleCard


class SaleCardImage(models.Model):
    salecard: models.ForeignKey = models.ForeignKey(SaleCard, related_name="images", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="images_manager/image_folder/salecard/")

    def __str__(self):
        return f"Image for {self.salecard.title}"
