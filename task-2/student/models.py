from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length =100)
    last_name = models.CharField(max_length =100)
    class_number = models.IntegerField()
    age = models.IntegerField()
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'student'