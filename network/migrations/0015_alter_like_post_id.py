# Generated by Django 3.2.3 on 2021-08-05 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20210805_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post', to='network.post'),
        ),
    ]
