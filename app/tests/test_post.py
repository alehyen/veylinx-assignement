from django.contrib.auth.models import User
import pytest

from app.models import Post, Hashtag
from app.utils import get_old_posts


@pytest.mark.django_db
def test_create_user(anonymous_client):
    payload = {
        "username": "test_user",
        "password": "test_user"
    }
    assert User.objects.count() == 0
    res = anonymous_client.post('/api/create_user/', data=payload)
    assert res.status_code == 201
    assert User.objects.count() == 1


@pytest.mark.parametrize(
    "url",
    [
        '/api/posts/',
        '/api/users/1/posts/'
    ]
)
def test_unauthorized_access(anonymous_client, url):
    res = anonymous_client.get(url)
    assert res.status_code == 401


def test_create_post(authenticated_client):
    payload = {
        "text": "Best Post ever #best"
    }
    assert Post.objects.count() == 0
    res = authenticated_client.post('/api/posts/', data=payload)
    assert res.status_code == 201
    assert Post.objects.count() == 1
    assert Hashtag.objects.count() == 1


def test_update_post(authenticated_client, test_post):
    post = test_post
    assert post.text == 'this is a post'
    payload = {
        'id_post': post.id_post,
        'text': 'this a modified post'
    }
    res = authenticated_client.put('/api/posts/', data=payload)
    post.refresh_from_db()
    assert res.status_code == 200
    assert post.text == 'this a modified post'


def test_delete_post(authenticated_client, test_post):
    post = test_post
    payload = {
        'id_post': post.id_post,
    }
    res = authenticated_client.delete('/api/posts/', data=payload)
    post.refresh_from_db()
    assert res.status_code == 200
    assert post.deleted


def test_bad_parameters(authenticated_client):
    import json
    payload = {
        "name": "Best Post ever"
    }
    res = authenticated_client.post('/api/posts/', data=payload)
    assert res.status_code == 400
    assert 'text' in json.loads(res.content)


def test_get_old_posts(old_posts):
    p1, p2 = old_posts
    old = get_old_posts(older_than=10)
    assert p1.id_post in old
    assert p2.id_post not in old
