# Generated by Django 4.0.2 on 2022-02-23 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_customuser_image_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/5b5e8482-50e2-4ddf-a7b8-352a9a68b5c8'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/f9fa927f-cbd3-4334-a15f-4b90f5e79a48'),
        ),
    ]