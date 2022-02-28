
from user.models import *
from Doctors.models import *
from Departments.models import *
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class Userser(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields=('username','email','password','fullname','image','report','date_of_birth','is_superuser','is_active','last_login','date_joined','age','address','is_staff','id','phone','doctor_id','gender','guardian_number','guardian_relation')
        # exclude=('groups','user_permissions')

        # extra_kwargs ={
        #     'password':{'write_only':True}
        # }
        
class Doctorser(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        

class Appointmentser(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class Departmentser(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'
        


class Commentser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'