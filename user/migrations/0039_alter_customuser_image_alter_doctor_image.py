# Generated by Django 4.0.2 on 2022-02-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0038_alter_customuser_image_alter_customuser_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/51b139c7-7c9a-4c8e-b057-09e0fd59effc'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/4866d5c6-b1c4-43be-a625-fa03b017cafe'),
        ),
    ]