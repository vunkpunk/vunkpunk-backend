from django.urls import reverse
from rest_framework import serializers
from vp_users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "dormitory", "faculty", "description", "photo")
        read_only_fields = ("username",)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get("request")

        # Получаем имя файла из поля photo
        photo_name = instance.photo.name if instance.photo else None

        if photo_name:
            # Строим URL вашего специального маршрута
            url = reverse("salecard_image", args=(instance.pk,))
            # Создаем полный URL
            full_url = request.build_absolute_uri(url)
            representation["photo"] = full_url
        else:
            representation["photo"] = None

        return representation
