# Generated by Django 3.2.12 on 2022-05-22 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220520_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie_poster',
            field=models.ImageField(blank=True, upload_to='poster_images/'),
        ),
    ]
