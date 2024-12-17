from django.urls import reverse
from images_manager.models import SaleCardImage
from rest_framework import serializers


class SaleCardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleCardImage
        fields = ("id", "photo")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")
        url = reverse("salecard_image", args=(instance.pk,))
        full_url = request.build_absolute_uri(url)
        representation["photo"] = full_url

        return representation
