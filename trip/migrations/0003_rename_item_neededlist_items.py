# Generated by Django 5.1.1 on 2024-10-09 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='neededlist',
            old_name='item',
            new_name='items',
        ),
    ]
