# Generated by Django 5.1.3 on 2024-11-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_remove_car_power'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='colors',
            field=models.ManyToManyField(to='cars.color'),
        ),
    ]