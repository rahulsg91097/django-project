# Generated by Django 4.2.3 on 2023-07-09 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='image',
        ),
    ]
