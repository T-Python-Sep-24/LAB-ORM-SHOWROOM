# Generated by Django 5.1.3 on 2024-11-22 12:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('cars', '0004_brand_alter_car_available_colors_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='brands.brand'),
        ),
    ]