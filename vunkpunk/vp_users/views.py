from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from vp_users.models import User
from vp_users.serializers import UserSerializer


class UserRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(), )
        return (permissions.IsAdminUser(), )
