# Generated by Django 4.0.2 on 2022-02-22 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/a04b3b26-5c5d-4314-aed4-0237df1617a2'),
        ),
    ]