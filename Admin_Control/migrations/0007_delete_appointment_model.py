# Generated by Django 5.0.7 on 2024-08-04 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Control', '0006_remove_appointment_model_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment_Model',
        ),
    ]
