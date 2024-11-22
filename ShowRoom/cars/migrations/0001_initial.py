# Generated by Django 5.1.3 on 2024-11-22 11:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0002_remove_brand_segment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hexadecimal_color', models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('photo', models.ImageField(upload_to='images/')),
                ('specs', models.TextField()),
                ('model', models.CharField(max_length=254)),
                ('segment', models.CharField(choices=[('economy', 'Economy'), ('luxury', 'Luxury'), ('sports', 'Sports'), ('electric', 'Electric'), ('sedan', 'Sedan'), ('wagon', 'Wagon'), ('premium', 'Premium'), ('suv', 'Sport Utility Vehicle'), ('minivan', 'Minivan'), ('crossover', 'Crossover')], max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('currency', models.CharField(default='SAR', max_length=5)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.brand')),
                ('color', models.ManyToManyField(to='cars.color')),
            ],
        ),
        migrations.CreateModel(
            name='VehiclePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.car')),
            ],
        ),
    ]