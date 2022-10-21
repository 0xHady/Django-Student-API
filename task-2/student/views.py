from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Student
import json

# remove later
def fuck(request):
    return HttpResponse("fuck")

# Create your views here.
class StudentV(View):
    def get(self,request):
        data = Student.objects.all()
        if(data.count()):
            return JsonResponse({'students':list(data.values())})
        return JsonResponse({'Error':'no students available'})

    def post(self,request):
        pass


class StudentID(View):
    def get(self,request, *args, **kwargs):
        pass

    def put(self,request, *args, **kwargs):
        pass

    def delete(self,request, *args, **kwargs):
        pass