from django.shortcuts import render
from rest_framework import generics
from vp_forum.models import SaleCard
from vp_forum.serializers import SaleCardSerializer


class SaleCardApiView(generics.ListAPIView):
    queryset = SaleCard.objects.all()
    serializer_class = SaleCardSerializer
