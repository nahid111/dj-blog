from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User, Category, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'created_at', 'posts']
        read_only_fields = ['created_at', 'posts']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']
        read_only_fields = ['created_at']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        read_only_fields = ['created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(RegisterSerializer, self).create(validated_data)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    categories = serializers.StringRelatedField(many=True)
    comments = serializers.StringRelatedField(many=True)

    def to_internal_value(self, data):
        post_data = {
            "title": data.get('title'),
            "body": data.get('body'),
            "author": User.objects.get(pk=int(data.get('author')))
        }
        if data.get('cover_img_url', None):
            post_data['cover_img_url'] = data.get('cover_img_url')
        if data.get('categories', None):
            post_data['categories'] = [int(c) for c in data.get('categories')]
        return post_data

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'body', 'cover_img_url', 'created_at', 'updated_at', 'categories', 'comments']
        read_only_fields = ['id', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at']
