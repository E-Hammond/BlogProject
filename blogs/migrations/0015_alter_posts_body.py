# Generated by Django 3.2.2 on 2021-05-23 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0014_alter_posts_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='body',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
    ]
