from django.db import models
import datetime

# Create your models here.

class Person(models.Model):
  firstName = models.CharField(max_length = 50)
  middleName = models.CharField(max_length = 50)
  lastName = models.CharField(max_length = 50)
  street = models.CharField(max_length = 50)
  barangay = models.CharField(max_length = 50)
  city = models.CharField(max_length = 50)
  province = models.CharField(max_length = 50)
  zipCode = models.IntegerField()
  country = models.CharField(max_length = 50)
  birthdate = models.DateField()
  status = models.CharField(max_length = 15)
  gender = models.CharField(max_length = 10)
  spouseName = models.CharField(max_length = 50)
  spouseOccupation = models.CharField(max_length = 50)
  childrenNum = models.IntegerField()
  motherName = models.CharField(max_length = 50)
  motherOccupation = models.CharField(max_length = 50)
  fatherName = models.CharField(max_length = 50)
  fatherOccupation = models.CharField(max_length = 50)
  height = models.DecimalField(max_digits=5, decimal_places = 2)
  weight = models.DecimalField(max_digits=5, decimal_places = 2)
  religion = models.CharField(max_length = 50)

  class Meta:
    db_table = "Person"

class Customer(Person):
  dateRegistered = models.DateField(default=datetime.date.today)
  profilePic = models.ImageField(null=True)

  class Meta:
    db_table = "Customer"