# Generated by Django 5.1.3 on 2024-11-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0005_alter_review_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
