from django.contrib import admin
from django.urls import path


#We leant how to create django project and runserver
# django-admin startproject <name>
# python manage.py runserver 

urlpatterns = [
    path('admin/', admin.site.urls),
]
