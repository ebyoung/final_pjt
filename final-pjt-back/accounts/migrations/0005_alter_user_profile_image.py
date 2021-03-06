# Generated by Django 3.2.12 on 2022-05-22 11:17

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=imagekit.models.fields.ProcessedImageField(default='profile_images/default_profile.png', upload_to='profile_images/'),
        ),
    ]
