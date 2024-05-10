
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
class Employee(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    registration_date = models.DateField()

class Administrator(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

class Department(models.Model):
    name = models.CharField(max_length=200)
    ability = models.CharField(max_length=200)
    position_id = models.CharField(max_length=100)

class Responsibility(models.Model):
    position = models.ForeignKey(Department, on_delete=models.CASCADE)
    description = models.TextField()

class Leave(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=100)
    responsible_employee = models.ForeignKey(Employee, related_name='leaves_responsible', on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, related_name='leaves', on_delete=models.CASCADE)











