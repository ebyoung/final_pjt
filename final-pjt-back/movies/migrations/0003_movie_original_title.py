# Generated by Django 3.2.12 on 2022-05-24 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_recommendations'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='original_title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
