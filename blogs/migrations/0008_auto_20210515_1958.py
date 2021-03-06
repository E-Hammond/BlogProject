# Generated by Django 3.2.2 on 2021-05-15 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20210515_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
        migrations.AlterField(
            model_name='posts',
            name='is_published',
            field=models.BooleanField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(max_length=255),
        ),
    ]
