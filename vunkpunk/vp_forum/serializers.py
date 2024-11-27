from django.urls import reverse
from rest_framework import serializers

from vp_forum.models import SaleCard


class SaleCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleCard
        fields = "__all__"
        read_only_fields = ("rating", "user")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")
        photo_name = instance.photo.name if instance.photo else None
        if photo_name:
            url = reverse("salecard_image", args=(instance.pk,))
            full_url = request.build_absolute_uri(url)
            representation["photo"] = full_url
        else:
            representation["photo"] = None

        return representation
