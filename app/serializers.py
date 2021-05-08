from rest_framework import serializers

from app.models import Post, Hashtag


class UserSignUpSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=False)


class PostCreateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


class PostEditSerializer(serializers.Serializer):
    id_post = serializers.IntegerField(required=True)
    text = serializers.CharField(required=True)


class PostDeleteSerializer(serializers.Serializer):
    id_post = serializers.IntegerField(required=True)


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ['name']


class PostSerializer(serializers.ModelSerializer):
    tags = HashtagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['text', 'created_at', 'tags']


class PopularHashtagSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    count = serializers.IntegerField(required=True)
