# Generated by Django 3.0.5 on 2020-04-29 10:37

import django.db.models.manager
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('restaurantview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='restaurant',
            managers=[
                ('Restaurant', django.db.models.manager.Manager()),
            ],
        ),
    ]
