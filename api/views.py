from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from user.models import *
from Doctors.models import *
from Departments.models import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User

# Create your views here.

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        # token['email'] = Customuser.email
        token['is_superuser'] = Customuser.is_superuser
        token['is_staff'] = Customuser.is_staff
        # print(token['username'])
        
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class User_view(viewsets.ModelViewSet):
    serializer_class = Userser
    # queryset = Customuser.objects.all()
    
    def get_queryset(self):
        user=Customuser.objects.all()
        return user
  
    def create(self, request,*args,**kwargs):
        data=request.data
        new_user=Customuser.objects.create(username=data['username'],password=data['password'],email=data['email'],fullname=data['fullname'],gender=data['gender'],
        phone=data['phone'],address=data['address'],age=data['age'],date_of_birth=data['date_of_birth'],guardian_relation=data['guardian_relation'],guardian_number=data['guardian_number'])
        new_user.save()
        for doctor in data['doctors']:
            doctor_obj=Doctor.objects.get(id=doctor['id'])
            new_user.doctors.add(doctor_obj)
        serializer=Userser(new_user)
        return Response(serializer.data)
        
   


    
class Doctor_view(viewsets.ModelViewSet):
    serializer_class = Doctorser
    queryset = Doctor.objects.all()
    
class Appointment_view(viewsets.ModelViewSet):
    serializer_class = Appointmentser
    queryset = Appointment.objects.all()
    
class Doctorapp_View(viewsets.ModelViewSet):
    serializer_class = DoctorAppser
    queryset = DoctorApp.objects.all()
    
class Department_View(viewsets.ModelViewSet):
    serializer_class = Departmentser
    queryset = Department.objects.all()
    
class UserProfile_View(viewsets.ModelViewSet):
    serializer_class=UserProfileSer
    queryset=Customuser.objects.all()
    
class Comment_view(viewsets.ModelViewSet):
    serializer_class = Commentser
    queryset = Comment.objects.all() 
    
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/token',
        '/api/token/refresh'
    ]
    return Response(routes)

