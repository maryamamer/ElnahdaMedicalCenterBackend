from django.db import models
from django.core.validators import RegexValidator
import uuid
from django.contrib.auth.models import AbstractUser, PermissionsMixin
# from django.contrib.auth.models import User
import datetime

from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,**extra_fields):
        """
        Create and save a User with the given email and password.
        """
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


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    image = models.ImageField(upload_to=f'images/{uuid.uuid4()}', blank=True)
    phone_regex = RegexValidator(
        regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(verbose_name="phone", null=True, validators=[
                             phone_regex], max_length=14)
    date_of_birth = models.DateField(null=True)
    address = models.TextField(null=True)
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

    # def save(self):
    #     encodedString = base64.b64encode(self.image.file.read())
    #     data = {"key": os.environ.get("IMG_BB"), "image": encodedString.decode("utf-8")}
    #     uploadedImageInfo = requests.post("https://api.imgbb.com/1/upload", data=data)
    #     jsonResponse = json.loads(uploadedImageInfo.text)
    #     self.image = jsonResponse["data"]["display_url"]
    #     super().save()


class Customuser(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    email = models.EmailField("email address", unique=True)
    report = models.FileField(upload_to='uploads/% Y/% m/% d/', null=True)
    phone_regex = RegexValidator(
        regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
    phone = models.CharField(verbose_name="phone", null=True, validators=[
                             phone_regex], max_length=14)
    date_of_birth = models.DateField(null=True)
    record_number = models.TextField(null=True)
    address = models.TextField(null=True)
    age = models.IntegerField(null=True)
    image = models.ImageField(upload_to=f'images/{uuid.uuid4()}', blank=True)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=30, choices=GENDER_CHOICES, null=True)
    # guardian = models.CharField(max_length=20,null=True)
    # Guardian_choices = (
    #     ('first degree', 'First Degree'),
    #     ('second degree', 'Second Degree'),
    # )
    # guardian_relation = models.CharField(max_length=30, choices=Guardian_choices)
    USERNAME_FIELD = "email"  # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def __str__(self):
        return self.email

    # id=models.AutoField(primary_key=True)
    # comment = models.CharField(max_length=250,null=True)

    # username=models.CharField(max_length=20)
    # email=models.EmailField(max_length=50)
    # password=models.CharField(max_length=16)


#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField(max_length=50)
#     username=models.CharField(max_length=20)
#     email=models.EmailField(max_length=50)
#     report = models.FileField(upload_to ='uploads/% Y/% m/% d/')
#     phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
#     phone = models.CharField(verbose_name="phone",null=True, validators=[phone_regex], max_length=14)
#     date_of_birth = models.DateField(null=True)
#     record_number = models.TextField()
#     address= models.TextField()
#     age = models.IntegerField()
#     GENDER_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#     )
#     gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
#     guardian = models.CharField(max_length=20,null=True)
#     Guardian_choices = (
#         ('first degree', 'First Degree'),
#         ('second degree', 'Second Degree'),
#     )
#     guardian_relation = models.CharField(max_length=30, choices=Guardian_choices)


# class Doctor(models.Model):
#     id=models.AutoField(primary_key=True)
#     fullname=models.CharField(max_length=50)
#     username=models.CharField(max_length=20)
#     email=models.EmailField(max_length=50)
#     image = models.ImageField(upload_to=f'images/{uuid.uuid4()}', blank=True)
#     phone_regex = RegexValidator(regex=r'^01[1|0|2|5][0-9]{8}$', message='phone must be an egyptian phone number...')
#     phone = models.CharField(verbose_name="phone",null=True, validators=[phone_regex], max_length=14)
#     date_of_birth = models.DateField(null=True)
#     address= models.TextField()
#     age = models.IntegerField()
#     GENDER_CHOICES = (
#         ('male', 'Male'),
#         ('female', 'Female'),
#     )
#     gender = models.CharField(max_length=30, choices=GENDER_CHOICES)
#     education_degree = models.CharField(max_length=30,null=False)
#     specialization = models.CharField(max_length=50,null=False)
#     achievements = models.TextField(null=True)
#     marital_status = (
#         ('single', 'Single'),
#         ('married', 'Married'),
#     )
#     status =  models.CharField(max_length=30, choices=marital_status)


class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField(null=True)
    patient_id = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)


class PatientAppointment(models.Model):
    app_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    patient_id = models.ForeignKey(Customuser, on_delete=models.CASCADE)


class DoctorAppointment(models.Model):
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    app_id = models.ForeignKey(Appointment, on_delete=models.CASCADE)


class Comment(models.Model):
    patient_id = models.ForeignKey(Customuser, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    comment_description = models.TextField(blank=True, null=True)
