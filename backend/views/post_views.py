from rest_framework import viewsets, permissions
from backend.models import Post
from backend.serializers import PostSerializer


class PostView(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
