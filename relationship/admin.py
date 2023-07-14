from django.contrib import admin
from relationship.models import Person,Aadhar,Car,CarModel,FuelType,CModel
# Register your models here.
admin.site.register([Person,Aadhar,Car,CarModel,FuelType,CModel])