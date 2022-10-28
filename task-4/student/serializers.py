from django.core.exceptions import ValidationError 
from rest_framework import serializers
from .models import Parent,Student,Subject


def check_age(value):
    if value < 10:
        return ValidationError("Age must be greater than or equal 10")

class StudentSerializer(serializers.ModelSerializer):
	Age = serializers.IntegerField(validators = [check_age])
	class Meta:
		model = Student
		fields='__all__'

class ParentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parent
		fields = "__all__"


class SubjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subject
		fields = "__all__"