# Generated by Django 4.0.2 on 2022-02-22 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/83b0436e-6a57-40f0-8bda-29b338ab8b3e'),
        ),
    ]
