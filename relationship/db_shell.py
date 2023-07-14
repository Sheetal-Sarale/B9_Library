# exec(open(r"D:\python\djangoprojects\B9_Library\relationship\db_shell.py").read())

# OneToOne Relationship

from relationship.models import* 

# Person.objects.create(name="Hanmant", age=33, mobile=9913489789, email="Hanmant@gmail.com")

# all = Person.objects.all()                  # all person queryset
# print(list(all))

# p1 = Person.objects.get(id=7)
# print(p1)

# from django.utils import timezone
# from datetime import date

# Aadhar.objects.create(aadhar_number=790562389540, address="Manali",DOB=date(1990, 6, 6), person=p1)  # 1st way
# Aadhar.objects.create(aadhar_number=790562389540, address="Manali",DOB=date(1990, 6, 6), person_id=4) # 2nd way
# Aadhar.objects.create(aadhar_number=790569866765, address="Latur",DOB=date(1996, 7, 23))              # 3rd way

# a1 = Aadhar.objects.get(aadhar_number=790569866765)
# print(a1)

# a1.person = p1
# a1.save()


# Aadhar se person fetch kiya

# a1 = Aadhar.objects.get(id=6)
# print(a1.person.email)

# a1 = Aadhar.objects.get(aadhar_number=790562389540)
# print(a1.person)     (Person.objects.get(aadhar=a1))

# person se aadhar

# p1 = Person.objects.get(id=4) 
# print(p1.aadhar.address)
# print(p1.__dict__)


# code optimizations:-
# select related


# a1 = Aadhar.objects.select_related("person")#.get(aadhar_number=790562389540)
# print(list(a1))

# for i in Aadhar.objects.all().select_related("person"):
#     print(i.person)

# for p in Person.objects.all().select_related("aadhar_num"):
#     print(p.aadhar_num)
#
# -------------------------------------------------------------------------------------------------------------------------

# OneToMany Relationship

# from relationship.models import Car, CarModel

# mercedes = Car.objects.create(name="Tata")
# bmw = Car.objects.create(name="Hundai")

# data = Car.objects.all()
# print(data)


# c180 = CarModel.objects.create(name="c180", car=mercedes)
# print(c180)
# c200 = CarModel.objects.create(name="c200", car=mercedes)
# print(c200)

# bmw = Car.objects.get(name="bmw")

# x1 = CarModel.objects.create(name="x1", car=bmw)
# print(x1)

# x2 = CarModel.objects.create(name="x2", car=bmw)
# print(x2)

# tata = Car.objects.get(name="tata")

# nexon = CarModel.objects.create(name="nexon", car=tata)
# print(nexon)

# punch = CarModel.objects.create(name="punch", car=tata)
# print(punch)




# hundai = Car.objects.get(name="hundai")

# creta = CarModel.objects.create(name="creta", car=hundai)
# print(creta)

# aura = CarModel.objects.create(name="aura", car=hundai)
# print(aura)

# carmodel se car fetch

# c180 = CarModel.objects.get(name="c180")
# print(c180.car)

# creata = CarModel.objects.get(id=7)
# print(creata.car)

# mercedes = Car.objects.get(name="mercedes")
# print(mercedes.carmodels.all())

# b1 = Car.objects.get(id=2)
# print(b1.carmodels.all())

# t1 = Car.objects.get(name="tata")
# print(t1.carmodels.all())

# hundai = Car.objects.get(name="hundai")
# hundai.carmodels.add(verna)

# print(h1.carmodel_set.all())       # if  related name not provided

# nios = CarModel.objects.create(name="nios")
# nios.car = hundai
# nios.save()

# c200=CarModel.objects.get(name="c200")
# print(c200.car.name)

# bmw = Car.objects.get(name="bmw")
# x2 = CarModel.objects.get(name="x2")
# # print(x2.car)

# p1 = CarModel.objects.filter(car__name="mercedes")
# print(p1)

# c1 = Car.objects.filter(carmodels__name="creta")
# print(c1)

# p1 = CarModel.objects.filter(car__name__startswith="T")
# print(p1)

# h1 = Car.objects.filter(carmodels__name__endswith="s")
# print(h1)

# model = CarModel.objects.filter(car__name__in=["BMW","mercedes"])
# print(model)

# mercedes.carmodels.clear()
# Car.objects.get(name="hundai").delete()

# cm = CarModel.objects.get(id=2)
# mercedes.carmodels.remove(cm)
# -----------------------------------------------------------------------------------------------------------------------

# ManyToMany Relationship

from relationship.models import*

# c180 = CModel.objects.create(name="c180")
# c200 = CModel.objects.create(name="c200")
# print(CModel.objects.all())

# Disel = FuelType.objects.create(name="Disel")
# Gas = FuelType.objects.create(name="Gas")
# Hybrid = FuelType.objects.create(name="Hybrid")
# print(FuelType.objects.all())


# c180 = CModel.objects.get(name="c180")
# Gas = FuelType.objects.get(name="Gas")
# # c180.fueltype.add(Gas)
# print(c180.fueltype.all())

# c180 = CModel.objects.get(name="c180")
# disel= FuelType.objects.get(name="Disel")
# c180.fueltype.add(disel)

# c200 = CModel.objects.get(name="c200")

# disel= FuelType.objects.get(name="Disel")
# Gas = FuelType.objects.get(name="Gas")
# Hybrid = FuelType.objects.get(name="Hybrid")

# c200.fueltype.add(disel,Gas,Hybrid)

# print(c200.fueltype.all())

# c200.fueltype.create(name="Bio Disel")# create and assign the fueltype to the cmodel

# print(Gas.cmodel_set.all())

# print(FuelType.objects.get(name="Gas").cmodel_set.all())

# all = CModel.objects.filter(fueltype__name__startswith="B")
# print(all.query)

# c180 = CModel.objects.get(name="c180")
# c180.fueltype.clear()

# c180.fueltype.set([Disel,Gas])