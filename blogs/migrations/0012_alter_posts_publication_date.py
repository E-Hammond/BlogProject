# Generated by Django 3.2.2 on 2021-05-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0011_alter_categories_category_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='publication_date',
            field=models.DateTimeField(),
        ),
    ]
