# Generated by Django 3.2.3 on 2021-08-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
    ]
