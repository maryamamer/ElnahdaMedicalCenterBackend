from django.contrib import admin
from .models import Doctor, Customuser, Appointment
from django.contrib.auth.admin import UserAdmin

admin.site.register(Appointment)
admin.site.register(Doctor)

class CustomUserAdmin(UserAdmin):
    model = Customuser
    list_display = ['id','username','email','phone','date_of_birth','address','age','gender','fullname']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('phone','date_of_birth','address','age','gender','fullname')}),
)

admin.site.register(Customuser, CustomUserAdmin)

# Register your models here.


''' class CustomUserAdmin(UserAdmin):
    model = Customuser
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Other Personal info',
            None,
            {
                'fields': [
                    'id',
                    'email',
                    'phone',
                    'date_of_birth',
                    'report',
                    'address',
                    'GENDER_CHOICES'
                ]
            }
        )
    )
admin.site.register(Customuser, CustomUserAdmin)
'''