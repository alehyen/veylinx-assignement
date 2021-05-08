from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.models import Post
from app.views import create_user, PostView, UsersPostView, HashtagPostsView, \
    popular_hashtags

admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_user/', create_user),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/posts/', PostView.as_view()),
    path('api/users/<int:user_id>/posts/', UsersPostView.as_view()),
    # Note: because hashtags begins with # and this character is prohibited
    # from urls (see https://www.ietf.org/rfc/rfc1738.txt) you need to encode it
    # (the encode of # is %23) or send just the hashtag without #,
    # I'll go with the latest solution
    path('api/hashtags/<str:hashtag>/posts/', HashtagPostsView.as_view()),
    path('api/popular_hashtags/', popular_hashtags),
]
