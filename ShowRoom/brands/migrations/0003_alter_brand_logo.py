# Generated by Django 5.1.3 on 2024-11-22 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0002_alter_brand_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(default='images/default.jpg', upload_to='images/brands/'),
        ),
    ]