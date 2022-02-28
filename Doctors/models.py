from django.db import models
import uuid
from django.core.validators import RegexValidator
import datetime
import django
from Departments.models import Department

# Create your models here.

class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    experience=models.IntegerField(default='1')
    username = models.CharField(max_length=50,unique=True,default='none')
    password=models.CharField(max_length=20,default='0')
    fullname =models.CharField(max_length=50,null=True)
    email = models.EmailField("email address", unique=True,default='abcd@gmail.com')
    phone_regex = RegexValidator(
        regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(verbose_name="phone", null=True, validators=[
                             phone_regex], max_length=14)
    date_of_birth = models.DateField(null=True,default=django.utils.timezone.now)
    address = models.TextField(null=True)
    image = models.ImageField(upload_to=f'images/{uuid.uuid4()}', blank=True)
    price = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
    education_degree = models.CharField(max_length=30, null=False)
    specialization = models.CharField(max_length=50, null=False)
    achievements = models.TextField(null=True)
    marital_status = (
        ('single', 'Single'),
        ('married', 'Married'),
    )
    status = models.CharField(max_length=30, choices=marital_status)
    is_superuser=models.BooleanField(null=True)
    dept_id=models.ForeignKey(Department,null=True,on_delete=models.CASCADE)
    patient_number=models.IntegerField(null=True)
    
class DoctorApp(models.Model):
    id=models.AutoField(primary_key=True)
    doctor_id=models.ForeignKey(Doctor,null=True,on_delete=models.CASCADE)
    date=models.DateTimeField(default=django.utils.timezone.now)
