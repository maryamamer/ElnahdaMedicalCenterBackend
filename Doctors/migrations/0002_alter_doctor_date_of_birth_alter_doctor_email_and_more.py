# Generated by Django 4.0.2 on 2022-03-03 14:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='abcd@gmail.com', max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='fullname',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/6f32cf95-17f7-42a0-9bfb-ea737c0fc8bf'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='password',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='username',
            field=models.CharField(default='none', max_length=50, unique=True),
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
