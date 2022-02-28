from django.db import models

# Create your models here.

class Department (models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(null=False,max_length=250)
    number_of_doctors = models.IntegerField(null=True)
    
