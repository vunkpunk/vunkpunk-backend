from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from vp_forum.models import SaleCard
from vp_forum.serializers import SaleCardSerializer
from vp_users.permissions import IsAuthor


class SaleCardViewSet(viewsets.ModelViewSet):
    queryset = SaleCard.objects.all()
    serializer_class = SaleCardSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["user_id"] = request.user.id
        serializer.validated_data["rating"] = 5.0
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_permissions(self):
        permission_classes = [IsAuthenticated if self.action in {"list", "create"} else IsAuthor]
        return [permission() for permission in permission_classes]
