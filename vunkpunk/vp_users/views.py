from django.shortcuts import render
from rest_framework import viewsets
from vp_users.models import User
from vp_users.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
