# Generated by Django 3.2.3 on 2021-08-03 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20210804_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='following',
            name='user_main',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='main_user', to='network.user'),
            preserve_default=False,
        ),
    ]
