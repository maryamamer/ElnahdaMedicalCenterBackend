# Generated by Django 4.0.2 on 2022-02-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_customuser_image_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/499e23ef-7cf6-4442-b1bb-d4ae6ffc8c19'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/96fb4747-e600-4fdd-98e8-6198caf8c6a7'),
        ),
    ]
