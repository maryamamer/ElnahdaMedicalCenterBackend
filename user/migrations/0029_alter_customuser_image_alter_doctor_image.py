# Generated by Django 4.0.2 on 2022-02-23 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0028_alter_customuser_image_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/f25999af-7698-4a27-a36d-b16588da7468'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/1e8554cc-f993-4182-94b5-58e8d74a6f34'),
        ),
    ]