# Generated by Django 4.0.2 on 2022-02-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_alter_customuser_image_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/0deb827b-8f20-466a-8179-ccf362394610'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/2f1eb787-7e07-485b-9b34-275ce93d20da'),
        ),
    ]