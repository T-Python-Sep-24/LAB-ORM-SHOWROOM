# Generated by Django 5.0.7 on 2024-07-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=256)),
                ('rating', models.SmallIntegerField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]
