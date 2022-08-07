from ctypes.wintypes import HANDLE
from email.mime import audio
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.
#extending the base User model with two new fields using abstract user
class User(AbstractUser):
    is_student=models.BooleanField(default=False)
    is_teacher=models.BooleanField(default=False)
   #student model
class student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    standard=models.IntegerField()
    section=models.CharField(max_length=1)
    stream=models.CharField(max_length=100)
    roll_no=models.IntegerField()
    
   #teacher model
class teacher(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key = True)
    subject=models.CharField(max_length=100)
    class_taught=models.IntegerField() 
    contact_number=models.CharField(max_length=10)



