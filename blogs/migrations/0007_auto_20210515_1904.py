# Generated by Django 3.2.2 on 2021-05-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20210515_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(max_length=100),
        ),
    ]
