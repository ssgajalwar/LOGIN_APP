# Generated by Django 5.0.1 on 2024-03-24 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0008_student_ip_addr'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='inrange',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
