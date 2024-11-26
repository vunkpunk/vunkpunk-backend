from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from vp_forum.models import SaleCard
from vp_users.models import User


@api_view(["GET"])
def image_profile(request, user_id):
    image = User.objects.get(pk=user_id).photo
    return HttpResponse(image, content_type="image/png")


@api_view(["GET"])
def image_salecard(request, salecard_id):
    image = SaleCard.objects.get(pk=salecard_id).photo
    return HttpResponse(image, content_type="image/png")
