# Generated by Django 5.1.1 on 2024-10-21 11:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0002_remove_route_places_place_route'),
        ('trip', '0003_alter_trip_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='trip.trip'),
        ),
    ]
