# Generated by Django 5.0.7 on 2024-08-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Randevu', '0004_alter_weekly_randevu_model_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_randevu_model',
            name='start_time',
            field=models.TimeField(default='09:01:10'),
        ),
    ]
