# Generated by Django 3.2.3 on 2021-08-05 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_alter_like_post_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
