# Generated by Django 4.0.2 on 2022-02-22 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_customuser_managers_alter_customuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/196aac73-437d-4146-9765-3d05f54e41c6'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/b670120e-f685-4453-b232-13a097e4bee9'),
        ),
    ]
