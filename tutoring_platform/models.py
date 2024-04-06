from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    first_name = first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=50)
    age_group = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

