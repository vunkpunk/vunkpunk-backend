from django.urls import reverse
from rest_framework import serializers
from vp_comments.models import Comment


class CommentsSerializer(serializers.ModelSerializer):
    user_link = serializers.SerializerMethodField("get_user_link")

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ("user", "post")

    def get_user_link(self, instance):
        request = self.context.get("request")
        return request.build_absolute_uri(reverse("user", args=(instance.user.pk,)))
