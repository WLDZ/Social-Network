# Generated by Django 4.2.7 on 2023-11-29 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile_picture',
            name='image_data',
            field=models.BinaryField(null=True),
        ),
    ]
