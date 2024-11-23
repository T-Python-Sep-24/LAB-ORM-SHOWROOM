# Generated by Django 5.1.3 on 2024-11-23 11:11

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_car_image_car_name_car_photo_car_specs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='specs',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
         migrations.AlterField(
    model_name='car',
    name='year',
    field=models.IntegerField(default=2000),  # Correct default
),



        migrations.AlterField(
            model_name='color',
            name='hex_code',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
