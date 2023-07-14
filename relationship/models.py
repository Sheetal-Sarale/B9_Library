from django.db import models

# Create your models here.

#OneToOne Relationship

class Person(models.Model):    # person_object.aadhar  (person se aadhar fetch) in case of related name is provided person_object.aadhar_num
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(null=True, unique=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.name 
       



class Aadhar(models.Model): # aadhar_object.person   (aadhar se person fetch)
    aadhar_number = models.BigIntegerField(unique=True)
    address= models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now=True)
    DOB = models.DateField()
    is_active = models.BooleanField(default=True)
    # is_updated = models.DateTimeField(auto_now=True)
    # created_by = models.CharField(max_length=100)
    # updated_by = models.CharField(max_length=100)
    person = models.OneToOneField(Person, on_delete=models.CASCADE, null=True, related_name="aadhar_num")     # person class

    class Meta:
        db_table = "aadhar"
    
    
    def __str__(self):
        return str(self.aadhar_number)
       

# OneToMany Relationship:-  
# 
class Car(models.Model):     # car_object.carmodel_set.all()         if related name provided car_object.carmodels
    name = models.CharField(max_length=100, unique=True)

    
    class Meta:
        db_table = "car"
    
    

    def __str__(self):
        return self.name
    

class CarModel(models.Model):
    name = models.CharField(max_length=100)    
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True, related_name="carmodels")

    
    class Meta:
        db_table = "car_model"
    
    
             
    def __str__(self):
        return self.name



class FuelType(models.Model):
    name = models.CharField(max_length=255)   


    class Meta:
        db_table = "fuel_type"

             
    def __str__(self):
        return self.name
    


class CModel(models.Model):
    name = models.CharField(max_length=255)
    # fueltype = models.ManyToManyField(FuelType)  # id(pk),fuel_type_id(fk), cmodel_id(fk)



    # class Meta:
    #     db_table = "cmodel"

             
    # def __str__(self):
    #     return self.name
    
# substitute for manytomany
class CModel_Fueltype(models.Model) :
    cmodel = models.ForeignKey(CModel,on_delete=models.SET_NULL, null=True)
    fueltype = models.ForeignKey(FuelType,on_delete=models.SET_NULL, null=True)
    extra_field = models.CharField(max_length=200)

    class Meta:
        unique_together = (('cmodel','fueltype'),)  # composite key


# id fueltype_id, cmodel_id, extra_field        




# ERD--Entity relationsdhip diagram
    

    
         
    
