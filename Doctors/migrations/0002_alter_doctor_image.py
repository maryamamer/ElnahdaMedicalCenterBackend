# Generated by Django 4.0.2 on 2022-02-27 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/cc2b609e-1b18-47a9-a55c-8a4c30091951'),
        ),
    ]