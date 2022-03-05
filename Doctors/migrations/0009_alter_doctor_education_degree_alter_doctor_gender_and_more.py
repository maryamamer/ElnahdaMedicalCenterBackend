# Generated by Django 4.0.2 on 2022-03-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0008_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='education_degree',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/a4f4e688-280c-4029-a086-864664182597'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married')], max_length=30, null=True),
        ),
    ]