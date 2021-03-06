# Generated by Django 4.0.2 on 2022-03-03 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0006_alter_doctor_image'),
        ('user', '0005_alter_customuser_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='doctor_ids',
            field=models.ManyToManyField(blank=True, null=True, to='Doctors.Doctor'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/4feb32ed-e3b5-448b-b840-54d3cd84dfb6'),
        ),
    ]
