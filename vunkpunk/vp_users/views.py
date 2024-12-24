import random

import requests
from django.conf import settings
from django.core.mail import send_mail
from django.utils.timezone import now
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from vp_users.models import User
from vp_users.serializers import UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.IsAuthenticated(),)
        return (permissions.IsAdminUser(),)


class ActivateAccountView(APIView):
    def post(self, request):
        email = request.data.get("email")
        activation_code = request.data.get("activation_code")

        if request.data.get("resend") is True:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response(
                    {"detail": "Неверный email, не получится сгенерировать новый код."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            user.set_activation_code()  # Генерация кода активации

            # Отправляем код на email
            send_mail(
                subject="Ваш код активации",
                message=f"Ваш код активации: {user.activation_code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[user.email],
            )
            return Response({"detail": "Новый код выслан на почту."}, status=status.HTTP_200_OK)
        try:
            user = User.objects.get(email=email, activation_code=activation_code)
        except User.DoesNotExist:
            return Response({"detail": "Неверный код активации или email."}, status=status.HTTP_400_BAD_REQUEST)

        # Проверяем срок действия кода
        if user.activation_code_expires_at < now():
            return Response({"detail": "Код активации истёк."}, status=status.HTTP_400_BAD_REQUEST)

        # Активируем аккаунт
        user.is_active = True
        user.activation_code = None  # Код больше не нужен
        user.activation_code_expires_at = None
        user.save()

        return Response({"detail": "Аккаунт успешно активирован!"}, status=status.HTTP_200_OK)
