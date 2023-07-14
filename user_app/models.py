from django.db import models

# Create your models here.

# class Person(models.Model):    # person_object.aadhar  (person se aadhar fetch) in case of related name is provided person_object.aadhar_num
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(unique=True)
#     mobile = models.BigIntegerField(null=True, unique=True)
#     is_active = models.BooleanField(default=True)
