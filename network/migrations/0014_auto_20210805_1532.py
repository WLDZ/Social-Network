# Generated by Django 3.2.3 on 2021-08-05 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_auto_20210805_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='network.post'),
        ),
        migrations.AddField(
            model_name='like',
            name='post_like_user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='post_like', to='network.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='like',
            name='user_disliked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='like',
            name='user_liked',
            field=models.BooleanField(default=False),
        ),
    ]
