# Generated by Django 3.1.7 on 2021-07-13 09:58

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('new_trip', '0008_auto_20210713_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catch',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default_img.png', force_format='JPEG', keep_meta=False, null=True, quality=95, size=[1080, 1350], upload_to='catch_images/'),
        ),
    ]
