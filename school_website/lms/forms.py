from django import forms
from . import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class StudentUserForm(forms.ModelForm):
    class Meta:
        User = get_user_model()
        model=User
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.student
        fields=['standard','section','stream','roll_no']
class TeacherUserForm(forms.ModelForm):
    class Meta:
        User = get_user_model()
        model=User
        fields=['first_name','last_name','username','password']

class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.teacher
        fields=['subject','class_taught','contact_number']