# Generated by Django 5.1.1 on 2024-10-14 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0002_remove_tripbudget_trip'),
        ('trip', '0005_remove_trip_item_list_trip_item_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='budget',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='money.tripbudget'),
        ),
    ]
