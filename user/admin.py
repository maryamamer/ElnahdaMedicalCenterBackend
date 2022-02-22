from django.contrib import admin
from .models import Doctor,Customuser,Appointment
from django.contrib.auth.admin import UserAdmin

admin.site.register(Appointment)
admin.site.register(Doctor)

class CustomUserAdmin(UserAdmin):
    model = Customuser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff','age']

admin.site.register(Customuser, CustomUserAdmin)

# Register your models here.
