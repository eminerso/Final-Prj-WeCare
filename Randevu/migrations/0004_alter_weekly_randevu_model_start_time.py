# Generated by Django 5.0.7 on 2024-08-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Randevu', '0003_alter_weekly_randevu_model_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekly_randevu_model',
            name='start_time',
            field=models.CharField(default='09:01:10', max_length=10),
        ),
    ]
