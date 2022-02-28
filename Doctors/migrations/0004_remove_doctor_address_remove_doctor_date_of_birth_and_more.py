# Generated by Django 4.0.2 on 2022-02-28 08:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0003_alter_doctor_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='address',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='email',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='fullname',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='image',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='password',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='username',
        ),
        migrations.CreateModel(
            name='DoctorApp',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Doctors.doctor')),
            ],
        ),
    ]