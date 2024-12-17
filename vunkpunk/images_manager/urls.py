from django.urls import path
from images_manager.views import image_profile, image_salecard

urlpatterns = [
    path(r"user/<int:user_id>", image_profile, name="user_image"),
    path(r"salecard/<int:salecard_photo_id>", image_salecard, name="salecard_image"),
]
