from django.urls import reverse
from images_manager.models import SaleCardImage
from images_manager.serializers import SaleCardImageSerializer
from rest_framework import serializers
from vp_forum.models import SaleCard


class SaleCardSerializer(serializers.ModelSerializer):
    comments_link = serializers.SerializerMethodField("get_comments_link")
    images = serializers.ListField(
        child=serializers.ImageField(max_length=100, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False,
    )
    images_to_delete = serializers.ListField(child=serializers.IntegerField(), write_only=True, required=False)
    uploaded_images = SaleCardImageSerializer(source="images", many=True, read_only=True)

    class Meta:
        model = SaleCard
        fields = "__all__"
        read_only_fields = ("rating", "user")

    def create(self, validated_data):
        images_data = validated_data.pop("images", [])  # Извлекаем изображения
        post = SaleCard.objects.create(**validated_data)  # Создаём пост
        if not images_data:
            SaleCardImage.objects.create(
                salecard=post, photo="images_manager/image_folder/default/salecard_default.jpg"
            )
        for image_data in images_data:
            SaleCardImage.objects.create(salecard=post, photo=image_data)  # Добавляем изображения
        return post

    def update(self, instance, validated_data):
        # Обновляем текстовые данные поста
        instance.title = validated_data.get("title", instance.title)
        instance.price = validated_data.get("price", instance.price)
        instance.description = validated_data.get("description", instance.description)
        instance.contact = validated_data.get("contact", instance.contact)
        instance.dormitory = validated_data.get("dormitory", instance.dormitory)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.save()

        # Удаляем старые фотографии, если они переданы
        images_to_delete = validated_data.get("images_to_delete", [])
        print(images_to_delete)
        if images_to_delete:
            for image_id in images_to_delete:
                try:
                    image = SaleCardImage.objects.get(pk=image_id, salecard=instance)
                    image.photo.delete(save=False)  # Удаляем файл из файловой системы
                    image.delete()  # Удаляем запись из базы данных
                except SaleCardImage.DoesNotExist:
                    continue

        # Добавляем новые фотографии
        images = validated_data.get("images", [])
        for image in images:
            SaleCardImage.objects.create(salecard=instance, photo=image)

        return instance

    def get_comments_link(self, instance):
        request = self.context.get("request")
        return request.build_absolute_uri(reverse("comments_list", args=(instance.pk,)))
