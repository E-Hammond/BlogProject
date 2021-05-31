# Generated by Django 3.2.2 on 2021-05-29 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_alter_categories_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male')], default='Male', max_length=2),
        ),
    ]