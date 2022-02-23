from django.contrib.auth.models import User
from user.models import *
from rest_framework import serializers

class Userser(serializers.ModelSerializer):
    class Meta:
        model = Customuser
        fields = ('id','fullname','email','phone','date_of_birth','report','address','gender','age')
        extra_kwargs ={
            'password':{'write_only':True}
        }
        
class Doctorser(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        

class Appointmentser(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'
        
class PatientAppointmentser(serializers.ModelSerializer):
    class Meta:
        model = PatientAppointment
        fields = '__all__'

class DoctorAppointmentser(serializers.ModelSerializer):
    class Meta:
        model = DoctorAppointment
        fields = '__all__'

class Commentser(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'