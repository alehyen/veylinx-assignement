from celery import shared_task
from app.models import Post
from app.utils import get_old_posts

@shared_task
def send_welcome_email(email):
    """
        sending a welcome email will require configuring an email server
        which I believe is not relevant for the purpose of this assignment
        so I'm creating just the signature of the function
    """
    pass

@shared_task
def delete_old_posts(older_than):
    old_posts = get_old_posts(older_than=older_than)
    Post.objects.filter(id_post__in=old_posts).delete()
    return True
