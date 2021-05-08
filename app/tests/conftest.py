from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest
from rest_framework_simplejwt.tokens import RefreshToken

from app.models import Post


@pytest.fixture
def test_user(db):
    return User.objects.create_user(
        username="test",
        password="test"
    )


@pytest.fixture
def test_post(db, test_user):
    return Post.objects.create(
        owner=test_user,
        text="this is a post"
    )


@pytest.fixture
def anonymous_client():
    return APIClient()


@pytest.fixture
def authenticated_client(test_user):
    client = APIClient()
    refresh = RefreshToken.for_user(test_user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')
    return client


@pytest.fixture
def test_posts(db, authenticated_client):
    for text in [
        'lorem ipsum #hashtag #another_one',
        'lorem #hashtag ipsum',
        'hashtag #test'
    ]:
        authenticated_client.post('/api/posts/', data={'text': text})