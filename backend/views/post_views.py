from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.models import Post, User
from backend.serializers import PostSerializer, CommentSerializer, CategorySerializer


class PostList(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        author = User.objects.get(pk=request.user.id)
        categories = request.data.get('categories', [])
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=author, categories=categories)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, pk):
        post = self._get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self._get_object(pk)
        categories = request.data.get('categories', [])
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            if categories:
                serializer.save(categories=categories)
            else:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        post = self._get_object(pk)
        categories = request.data.get('categories', None)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            if categories:
                serializer.save(categories=categories)
            else:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self._get_object(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404


class PostCommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer

    def get(self, request, pk):
        post = self._get_object(pk)
        comments = post.comments
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def _get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404


class PostCategoriesView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer

    def get(self, request, pk):
        post = self._get_object(pk)
        categories = post.categories
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def _get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
