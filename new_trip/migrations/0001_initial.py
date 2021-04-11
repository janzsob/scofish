# Generated by Django 3.1.7 on 2021-04-03 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('lake', models.CharField(max_length=150, verbose_name='Lake')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='City')),
                ('s_date', models.DateTimeField(verbose_name='Starting Date')),
                ('e_date', models.DateTimeField(verbose_name='Ending Date')),
                ('trip_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name': 'Trip',
                'verbose_name_plural': 'Trips',
            },
        ),
        migrations.CreateModel(
            name='Fisherman',
            fields=[
                ('name', models.CharField(max_length=50, verbose_name='Fisherman')),
                ('fisherman_id', models.AutoField(primary_key=True, serialize=False)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.trips')),
            ],
            options={
                'verbose_name': 'Fisherman',
                'verbose_name_plural': 'Fishermen',
            },
        ),
        migrations.CreateModel(
            name='Catch',
            fields=[
                ('fish_type', models.CharField(max_length=50, verbose_name='Fish Type')),
                ('catch_id', models.AutoField(primary_key=True, serialize=False)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Weight')),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Length')),
                ('datetime', models.DateTimeField(verbose_name='Catch Time')),
                ('fisherman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.fisherman')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.trips')),
            ],
            options={
                'verbose_name': 'Catch',
                'verbose_name_plural': 'Catches',
            },
        ),
    ]
