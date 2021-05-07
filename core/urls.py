from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from app.models import Post
from app.views import create_user, PostView, UsersPostView

admin.site.register(Post)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/create_user/', create_user),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/posts/', PostView.as_view()),
    path('api/users/<int:user_id>/posts/', UsersPostView.as_view()),
]
