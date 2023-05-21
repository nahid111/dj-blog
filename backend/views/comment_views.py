from rest_framework import viewsets, permissions

from backend.models import Comment
from backend.serializers import CommentSerializer


class CommentView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
