# Generated by Django 5.0.1 on 2024-03-24 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0010_qrcodelog_city_qrcodelog_latitude_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institutes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('longitude', models.CharField(blank=True, max_length=255)),
                ('latitude', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
