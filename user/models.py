from django.db import models
from django.core.validators import RegexValidator
import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from django.contrib.auth.models import User
import datetime

from django.contrib.auth.base_user import BaseUserManager
from Departments.models import Department
from Doctors.models import Doctor

class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,**extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)

   


class Customuser(AbstractUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    fullname =models.CharField(max_length=50,null=True)
    email = models.EmailField("email address", unique=True)
    report = models.FileField(upload_to='uploads/% Y/% m/% d/', null=True)
    phone_regex = RegexValidator(
        regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(verbose_name="phone", null=True, validators=[
                             phone_regex], max_length=14)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to=f'images/{uuid.uuid4()}', blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True)
    guardian_number = models.CharField(max_length=20,null=True)
    Guardian_choices = (
        ('first degree', 'First Degree'),
        ('second degree', 'Second Degree'),
    )
    guardian_relation = models.CharField(max_length=30, choices=Guardian_choices,null=True)
    class Meta:
        abstact:True
    USERNAME_FIELD = "username" # make the user log in with the email
    # REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def __str__(self):
        return self.email
    

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    patient_id = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    comment_description = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True,null=True)
