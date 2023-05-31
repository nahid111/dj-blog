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
    author = serializers.StringRelatedField(required=False)
    categories = serializers.StringRelatedField(many=True, required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['id', 'author', 'categories', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['created_at']
