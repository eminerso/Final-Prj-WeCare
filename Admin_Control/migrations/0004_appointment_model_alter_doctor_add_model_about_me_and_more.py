# Generated by Django 5.0.7 on 2024-08-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_Control', '0003_alter_doctor_add_model_about_me_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=3)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('description', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['day', 'start_time'],
            },
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='about_me',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='education',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='last_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='my_skills',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor_add_model',
            name='speciality',
            field=models.CharField(max_length=80),
        ),
    ]
