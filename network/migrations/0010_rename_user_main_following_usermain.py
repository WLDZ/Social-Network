# Generated by Django 3.2.3 on 2021-08-04 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20210804_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='following',
            old_name='user_main',
            new_name='usermain',
        ),
    ]
