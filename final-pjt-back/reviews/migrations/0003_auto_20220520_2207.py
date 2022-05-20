# Generated by Django 3.2.12 on 2022-05-20 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_comment_re_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.review'),
        ),
        migrations.AlterField(
            model_name='review',
            name='watch_day',
            field=models.DateField(auto_now_add=True),
        ),
    ]