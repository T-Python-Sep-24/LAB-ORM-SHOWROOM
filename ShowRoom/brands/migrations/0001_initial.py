# Generated by Django 5.1.2 on 2024-11-20 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(default='images/default.jpg', upload_to='images/')),
                ('about', models.TextField()),
                ('founded_at', models.DateTimeField()),
            ],
        ),
    ]