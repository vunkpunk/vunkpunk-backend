from rest_framework import serializers
from vp_forum.models import SaleCard


class SaleCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleCard
        fields = "__all__"
        read_only_fields = ("rating", "user")
