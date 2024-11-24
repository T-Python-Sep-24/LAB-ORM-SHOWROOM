# Generated by Django 5.1.3 on 2024-11-24 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_review_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='cars.car'),
        ),
    ]
