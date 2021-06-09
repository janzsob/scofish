# Generated by Django 3.1.7 on 2021-06-03 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('new_trip', '0002_auto_20210520_1222'),
    ]

    operations = [
        migrations.CreateModel(
            name='HookBait',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Termék neve')),
                ('size', models.CharField(max_length=100, verbose_name='Méret')),
                ('taste', models.CharField(max_length=80, verbose_name='Íz')),
                ('fisherman', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_trip.fisherman')),
            ],
            options={
                'verbose_name': 'HookBait',
                'verbose_name_plural': 'HookBaits',
            },
        ),
    ]
