# Generated by Django 3.2.8 on 2024-01-16 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.DateField()),
                ('hourly', models.TimeField()),
                ('voltage_r', models.FloatField()),
                ('voltage_y', models.FloatField()),
                ('voltage_b', models.FloatField()),
                ('currents_r', models.FloatField()),
                ('currents_y', models.FloatField()),
                ('currents_b', models.FloatField()),
                ('power_r', models.FloatField()),
                ('power_y', models.FloatField()),
                ('power_b', models.FloatField()),
                ('temp', models.FloatField()),
                ('station_code', models.SlugField(max_length=255)),
            ],
            options={
                'get_latest_by': ['days', 'hourly', 'voltage_r', 'voltage_y', 'voltage_b', 'currents_r', 'currents_y', 'currents_b', 'power_r', 'power_y', 'power_b', 'temp', 'station_code'],
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255)),
                ('regional_office', models.CharField(max_length=255)),
                ('area_office', models.CharField(max_length=255)),
                ('station_name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('longtitudes', models.FloatField()),
                ('latitude', models.FloatField()),
                ('max_power', models.FloatField(max_length=255)),
                ('zipcode', models.IntegerField(null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('local_gov_area', models.CharField(max_length=225, null=True)),
                ('state', models.SlugField(max_length=225)),
                ('profile', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='region', to='iotPowerSystem.company')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('Company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='position', to='iotPowerSystem.company')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='level', to='iotPowerSystem.company')),
            ],
        ),
        migrations.CreateModel(
            name='AreaOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='area_office', to='iotPowerSystem.region')),
            ],
        ),
    ]
