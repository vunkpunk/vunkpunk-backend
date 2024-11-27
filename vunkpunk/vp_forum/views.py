from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from vp_forum.models import SaleCard
from vp_forum.serializers import SaleCardSerializer
from vp_users.permissions import IsAuthenticatedOrReadOnly, IsAuthor


class SaleCardsListCreateView(generics.ListCreateAPIView):
    # queryset = SaleCard.objects.all()
    serializer_class = SaleCardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        if self.request.GET:
            user_id = self.request.GET.get("user_id")
            if user_id:
                return SaleCard.published.all().filter(user_id=user_id)
            search = self.request.GET.get("search")
            if search:
                return SaleCard.published.all().filter(title__icontains=search)
        return SaleCard.published.all()

    def perform_create(self, serializer):  # TODO: фегово работает редирект после создания поста
        serializer.save(user_id=self.request.user.id, rating=5.0)


class SaleCardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleCard.objects.all()
    serializer_class = SaleCardSerializer
    permission_classes = (IsAdminUser | IsAuthor,)
