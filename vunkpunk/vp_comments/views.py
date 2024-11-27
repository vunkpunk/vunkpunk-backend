from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from vp_comments.models import Comment
from vp_comments.serializers import CommentsSerializer


class CommentsListView(generics.ListCreateAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Comment.objects.all().filter(post_id=self.kwargs.get("post_id")).order_by("-time_created")

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id, post_id=self.kwargs.get("post_id"))
