from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from vp_forum.models import Category, SaleCard
from vp_forum.serializers import CategorySerializer, SaleCardSerializer
from vp_users.permissions import IsAuthenticatedOrReadOnly, IsAuthor


class SaleCardsListCreateView(generics.ListCreateAPIView):
    serializer_class = SaleCardSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        result = SaleCard.objects.all()
        if self.request.GET:
            status = self.request.GET.get("published")
            if status == "true":
                result = SaleCard.published.all()
            elif status == "false":
                result = SaleCard.objects.filter(is_published=False)
            user_id = self.request.GET.get("user_id")
            if user_id:
                result = result.filter(user_id=user_id)
            search = self.request.GET.get("search")
            if search:
                result = result.filter(title__icontains=search)
        return result

    def perform_create(self, serializer):  # TODO: фегово работает редирект после создания поста
        serializer.save(user_id=self.request.user.id, rating=5.0)


class SaleCardRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = SaleCard.objects.all()
    serializer_class = SaleCardSerializer
    permission_classes = (IsAdminUser | IsAuthor,)


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
