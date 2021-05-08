from rest_framework import serializers

from app.models import Post


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class PostCreateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


class PostEditSerializer(serializers.Serializer):
    id_post = serializers.IntegerField(required=True)
    text = serializers.CharField(required=True)


class PostDeleteSerializer(serializers.Serializer):
    id_post = serializers.IntegerField(required=True)


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
