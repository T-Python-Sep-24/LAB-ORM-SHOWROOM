# Generated by Django 5.1.3 on 2024-11-24 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_alter_car_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='specs',
        ),
    ]
