# Generated by Django 3.1.7 on 2021-04-19 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Fisherman',
            fields=[
                ('fisherman_id', models.AutoField(primary_key=True, serialize=False)),
                ('catch_sum_weight', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fisherman',
                'verbose_name_plural': 'Fishermen',
            },
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('lake', models.CharField(max_length=150, verbose_name='Lake')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('s_date', models.DateTimeField(verbose_name='Starting Date')),
                ('e_date', models.DateTimeField(verbose_name='Ending Date')),
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
                ('total_catch_weight', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('num_of_fish', models.IntegerField(default=0)),
                ('maxi_catches', models.IntegerField(default=0)),
                ('ben_catches', models.IntegerField(default=0)),
                ('attila_catches', models.IntegerField(default=0)),
                ('david', models.IntegerField(default=0)),
                ('fisherman', models.ManyToManyField(to='new_trip.Fisherman')),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
        migrations.CreateModel(
            name='Catch',
            fields=[
                ('fish_type', models.CharField(choices=[('Carp', 'Carp'), ('Amur', 'Amur'), ('Bream', 'Bream'), ('Crucian', 'Crucian'), ('Catfish', 'Catfish')], default='Carp', max_length=50, verbose_name='Fish Type')),
                ('catch_id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight')),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Length')),
                ('hook_bait', models.CharField(max_length=100, verbose_name='Hook Bait')),
                ('datetime', models.DateTimeField(verbose_name='Catch Time')),
                ('image', models.ImageField(blank=True, null=True, upload_to='catch_images/')),
                ('fisherman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.fisherman')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.trips')),
            ],
            options={
                'verbose_name': 'Catch',
                'verbose_name_plural': 'Catches',
            },
        ),
    ]