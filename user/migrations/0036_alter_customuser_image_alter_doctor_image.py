# Generated by Django 4.0.2 on 2022-02-24 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0035_alter_customuser_image_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/02118573-606e-4d8a-ba53-68b6772488b7'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/53ab1613-a135-4128-86ea-2336339b59ff'),
        ),
    ]
