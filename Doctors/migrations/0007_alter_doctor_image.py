# Generated by Django 4.0.2 on 2022-03-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0006_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/9745be26-857c-4b56-9bef-8b8a2af0651c'),
        ),
    ]
