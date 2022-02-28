# Generated by Django 4.0.2 on 2022-02-27 10:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=50)),
                ('experience', models.IntegerField(default='1')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/4ca43cb8-5496-440b-ad0e-8d1413da8acd')),
                ('phone', models.CharField(max_length=14, null=True, validators=[django.core.validators.RegexValidator(message='phone must be an egyptian phone number...', regex='^01[1|0|2|5][0-9]{8}$')], verbose_name='phone')),
                ('date_of_birth', models.DateField(null=True)),
                ('address', models.TextField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('age', models.IntegerField(null=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=30)),
                ('education_degree', models.CharField(max_length=30)),
                ('specialization', models.CharField(max_length=50)),
                ('achievements', models.TextField(null=True)),
                ('status', models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=30)),
                ('is_superuser', models.BooleanField(null=True)),
                ('patient_number', models.IntegerField(null=True)),
                ('dept_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Departments.department')),
            ],
        ),
    ]