# Generated by Django 4.0.2 on 2022-02-24 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0032_doctor_experience_alter_customuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/9c8e7f90-89df-428f-8ec1-c7f6d4e5d829'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/1e418a2f-2b0d-4413-b83e-ab531e80dc8d'),
        ),
    ]