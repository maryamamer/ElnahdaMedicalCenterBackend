# Generated by Django 4.0.2 on 2022-02-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_customuser_image_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/f7f65a8a-f7ec-4400-b30d-b8772ae48a52'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/91b84c30-f8eb-4d58-a1c7-f2f41033d1ce'),
        ),
    ]
