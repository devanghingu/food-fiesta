# Generated by Django 3.0.2 on 2020-04-21 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurantview', '__first__'),
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminview', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('total_price', models.PositiveIntegerField()),
                ('status', models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Accepted'), (2, 'Rejected'), (3, 'Delivered')])),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Address')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantview.Delivery')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurantview.Restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orderitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.PositiveIntegerField()),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminview.Fooditem')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardview.Order')),
            ],
        ),
    ]
