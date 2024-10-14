# Generated by Django 5.0.7 on 2024-08-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Randevu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weekly_Randevu_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_email', models.EmailField(default='emin@mm.nn', max_length=30)),
                ('day', models.CharField(default='Monday', max_length=50)),
                ('patient_name', models.CharField(default='Emin', max_length=50)),
                ('start_time', models.TimeField(default='09:01:10')),
                ('endof_time', models.TimeField(default='09:01:10')),
                ('gender', models.CharField(max_length=10)),
                ('patient_email', models.EmailField(max_length=30)),
                ('tel', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Monday_Randevu_Model',
        ),
    ]
