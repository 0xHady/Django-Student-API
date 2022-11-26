from curses.ascii import islower
from django import forms 
from .models import *
from django.forms import ValidationError
import re

def check_email(value):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.match(email_regex,value) is None:
        raise ValidationError('email not valid')
    pass

def check_first_name(value):
    if re.match('^[a-z]+$',value[1:len(value)]) is None or islower(value[0]):
        raise ValidationError('first name not valid')

def check_last_name(value):
    if re.match('^[a-z]+$',value[1:len(value)]) is None or islower(value[0]):
        raise ValidationError('last name not valid')

def check_age(value):
    if value < 18:
        raise ValidationError('age must be greater than or equal 18')


class StudentF(forms.ModelForm):
    first_name = forms.CharField(max_length=100,validators=[check_first_name])
    last_name  = forms.CharField(max_length=100,validators=[check_last_name])
    email = forms.CharField(max_length=100,validators=[check_email])
    age = forms.IntegerField(validators=[check_age])

    class Meta:
        model: Student
        exclude = ['parent','subject']
        fields = "__all__"