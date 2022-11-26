from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Student
import json

# Create your views here.
class StudentV(View):
    def get(self,request):
        data = Student.objects.all()
        if(data.count()):
            return JsonResponse({'students':list(data.values())})
        return JsonResponse({'Error':'no students available'})

    def post(self,request):
        data = json.loads(request.body)
        Student.objects.create(**data)
        return JsonResponse({'Mesage':'Created Sucessfully'})

class StudentID(View):
    def get(self,request, *args, **kwargs):
        data = Student.objects.filter(id=kwargs['id'])
        return JsonResponse({'Student':data})

    def put(self,request, *args, **kwargs):
        student = Student.objects.filter(id=kwargs['id'])
        student.update(**json.loads(request.body))
        return JsonResponse({'Mesage':'updated Sucessfully'})

    def delete(self,request, *args, **kwargs):
        student = Student.objects.filter(id=kwargs['id'])
        student.delete()
        return JsonResponse({'Mesage':'deleted Sucessfully'})