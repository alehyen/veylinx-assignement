import pytest

from app.utils import get_hashtags
from app.models import Hashtag

@pytest.mark.parametrize(
    'text, hashtags',
    [
        ('lorem ipsum #hashtag #another_one', ['hashtag', 'another_one']),
        ('lorem #fs58  ipsum #1', ['fs58', '1'])
    ]
)
def test_get_hashtags(text, hashtags):
    assert get_hashtags(text) == hashtags


def test_get_all_posts_with_hashtag(authenticated_client, test_posts):
    import json
    res = authenticated_client.get('/api/hashtags/hashtag/posts/')
    assert res.status_code == 200
    json_res = json.loads(res.content)
    assert json_res.get('count') == 2


def test_popular_hashtags(authenticated_client, test_posts):
    import json
    res = authenticated_client.get('/api/popular_hashtags/')
    assert res.status_code == 200
    json_res = json.loads(res.content)
    assert json_res[0]['name'] == 'hashtag'
    assert json_res[0]['count'] == 2
    assert json_res[1]['count'] == 1


@pytest.mark.django_db
def test_no_duplicate_hashtags(test_posts):
    assert Hashtag.objects.filter(name='hashtag').count() == 1
