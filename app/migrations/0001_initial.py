# Generated by Django 3.2.2 on 2021-05-07 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('deleted', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
