from asyncio import constants
from tkinter.tix import Tree
from django.db import models

# Create your models here.


class Parent(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)

    def __str__(self):
        return self.first_name
    class Meta:
        db_table = 'parent'

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length =100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'subject'


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length =100,blank=False)
    last_name = models.CharField(max_length =100,blank=False)
    class_number = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(unique = True)

    parent = models.ForeignKey(Parent,related_name="students",null=True,on_delete=models.SET_NULL)
    subject = models.ManyToManyField(Subject,related_name="students")

    constraints = [
        models.CheckConstraint(
            name = 'age greater than 18',check=models.Q(age__gt=18)
        ),
    ]

    def __str__(self):
        return self.first_name
    class Meta:
        db_table = 'student'