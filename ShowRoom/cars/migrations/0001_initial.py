# Generated by Django 5.1.2 on 2024-11-21 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('engine', models.CharField(max_length=1024)),
                ('doors', models.SmallIntegerField(choices=[(2, 'Two Doors'), (3, 'Three Doors'), (4, 'Four Doors'), (5, 'Five Doors')])),
                ('category', models.CharField(choices=[('luxury', 'Luxury Car'), ('family', 'Family Car'), ('sport', 'Super Sport Car'), ('sedan', 'Sedan Car'), ('suv', 'SUV'), ('truck', 'Truck')], max_length=48)),
                ('year', models.DateField()),
                ('image', models.ImageField(upload_to='images/')),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='brands.brand')),
                ('colors', models.ManyToManyField(to='cars.color')),
            ],
        ),
    ]
