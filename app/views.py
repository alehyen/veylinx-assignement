from django.contrib.auth.models import User
from django.core.paginator import Paginator, InvalidPage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST,\
    HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from app.serializers import UserSignUpSerializer, PostCreateSerializer, \
    PostEditSerializer, PostDeleteSerializer, PostSerializer
from app.models import Post


@api_view(["Post"])
@permission_classes((AllowAny,))
def create_user(request):
    signup_serializer = UserSignUpSerializer(data=request.data)
    if not signup_serializer.is_valid():
        return Response(signup_serializer.errors, status=HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(
        username=signup_serializer.data["username"],
        password=signup_serializer.data["password"]
    )
    return Response(
        {
            "username": user.username
        },
        status=HTTP_201_CREATED)


class PaginatorMixin:
    def get_paginated_response(self, queryset, model_serializer):
        try:
            page_number = self.request.query_params.get('page', 1)
            page_size = self.request.query_params.get('page_size', 20)
            paginator = Paginator(queryset, page_size)
            page = paginator.page(page_number)
            serializer = model_serializer(page, many=True)
            return Response({
                "count": paginator.count,
                'has_next': page.has_next(),
                'has_previous': page.has_previous(),
                "result": serializer.data
            })
        except InvalidPage:
            return Response(
                {
                    "error": f"invalid page {page_number}"
                },
                status=HTTP_404_NOT_FOUND
            )


class PostView(PaginatorMixin, APIView):
    def get(self, request):
        return self.get_paginated_response(Post.objects.filter(deleted=False).order_by('-created_at'), PostSerializer)

    def post(self, request):
        post_serializer = PostCreateSerializer(data=request.data)
        if not post_serializer.is_valid():
            return Response(post_serializer.errors, status=HTTP_400_BAD_REQUEST)
        post = Post.objects.create(
            owner=request.user,
            text=post_serializer.data["text"]
        )
        return Response(
            {
                "id_post": post.id_post
            },
            status=HTTP_201_CREATED
        )

    def put(self, request):
        update_serializer = PostEditSerializer(data=request.data)
        if not update_serializer.is_valid():
            return Response(update_serializer.errors, status=HTTP_400_BAD_REQUEST)
        try:
            post = Post.objects.get(id_post=update_serializer.data['id_post'])
            post.text = update_serializer.data['text']
            post.save()
            return Response({'success': True})
        except Post.DoesNotExist:
            return Response(
                {
                    "error": f"Post with id {update_serializer.data['id_post']} not found"
                },
                status=HTTP_404_NOT_FOUND
            )

    def delete(self, request):
        delete_serializer = PostDeleteSerializer(data=request.data)
        if not delete_serializer.is_valid():
            return Response(delete_serializer.errors, status=HTTP_400_BAD_REQUEST)
        try:
            post = Post.objects.get(id_post=request.data['id_post'])
            post.deleted = True
            post.save()
            return Response({'success': True})
        except Post.DoesNotExist:
            return Response(
                {
                    "error": f"Post with id {request.data['id_post']} not found"
                },
                status=HTTP_404_NOT_FOUND
            )


class UsersPostView(PaginatorMixin, APIView):
    def get(self, request, user_id):
        try:
            owner = User.objects.get(id=user_id)
            return self.get_paginated_response(Post.objects.filter(owner=owner, deleted=False), PostSerializer)
        except User.DoesNotExist:
            return Response(
                {
                    "error": f'No user with id {user_id}'
                },
                status=HTTP_404_NOT_FOUND
            )
