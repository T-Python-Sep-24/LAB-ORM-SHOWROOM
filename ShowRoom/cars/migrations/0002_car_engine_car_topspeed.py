# Generated by Django 5.1.3 on 2024-11-21 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.CharField(default='To be Determined', max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='topSpeed',
            field=models.CharField(default='To be Determined', max_length=258),
            preserve_default=False,
        ),
    ]