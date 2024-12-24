from django.conf import settings
from django.core.mail import send_mail
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


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        extra_kwargs: dict = {
            "username": {
                "validators": [],
            },
        }
        fields = ("username", "email", "password")

    def validate(self, attrs):
        """
        Переопределяем валидацию, чтобы удалять неактивных пользователей до проверки.
        """
        username = attrs.get("username")
        email = attrs.get("email")

        existing_user = User.objects.filter(username=username, email=email, is_active=False).first()
        if existing_user:
            existing_user.delete()
        elif User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": "Этот username уже занят."})
        elif User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Этот email уже занят."})

        # Возвращаем данные для стандартной обработки
        return super().validate(attrs)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_active=False,  # Пользователь не активен до верификации
        )
        user.set_activation_code()  # Генерация кода активации

        # Отправляем код на email
        send_mail(
            subject="Ваш код активации",
            message=f"Ваш код активации: {user.activation_code}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
        )
        return user
