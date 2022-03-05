
from user.models import *
from Doctors.models import *
from Departments.models import *
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


        # exclude=('groups','user_permissions')

        # extra_kwargs ={
        #     'password':{'write_only':True}
        # }
        
class Doctorser(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        
class Userser(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields=('id','username','email','password','fullname','image','date_of_birth','age','address','phone','doctors','gender','guardian_number','guardian_relation') 
        depth=1 
    
    
    

class Appointmentser(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class Departmentser(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        
class DoctorAppser(serializers.ModelSerializer):
    class Meta:
        model = DoctorApp
        fields = '__all__'
        


class Commentser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class UserProfileSer(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields=('fullname','email','phone','address')