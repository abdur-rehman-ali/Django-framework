from django.contrib import admin
from .models import studentRegistration 

# Register your models here.

#Using model class name
# admin.site.register(studentRegistration)


#Using ModelAdmin class name
# class studentRegistrationModelAdmin(admin.ModelAdmin):
#     list_display = ['name','reg_no']

# admin.site.register(studentRegistration,studentRegistrationModelAdmin)

#Using ModelAdmin class name and decorator

@admin.register(studentRegistration)
class studentRegistrationModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','reg_no','cgpa']

