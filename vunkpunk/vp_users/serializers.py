from django.urls import reverse
from rest_framework import serializers
from vp_users.models import User


class UserSerializer(serializers.ModelSerializer):
    user_salecards_link = serializers.SerializerMethodField("get_user_salecards_link")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "dormitory",
            "faculty",
            "description",
            "photo",
            "user_salecards_link",
        )
        read_only_fields = ("username",)

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

    def get_user_salecards_link(self, instance):
        request = self.context.get("request")
        url = reverse("salecards_list")
        return request.build_absolute_uri(f"{url}?user_id={instance.pk}")
