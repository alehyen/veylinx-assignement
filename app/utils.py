from app.models import Post


def get_hashtags(text):
    import re
    return re.findall('#([A-Za-z0-9_]+)', text)


def get_old_posts(older_than):
    from datetime import timedelta
    from django.utils import timezone

    comparison_date = timezone.now() - timedelta(days=older_than)
    query = Post.objects.filter(created_at__lte=comparison_date).values('id_post')
    return [elm['id_post'] for elm in query]

