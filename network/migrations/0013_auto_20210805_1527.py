# Generated by Django 3.2.3 on 2021-08-05 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0012_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='post_id',
        ),
        migrations.RemoveField(
            model_name='like',
            name='post_like_user',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_disliked',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user_liked',
        ),
    ]