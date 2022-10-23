from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from .forms import *
from .models import *
import json

# Create your views here.

class StudentV(View):
    pass
    def get(self,request):
        data = Student.objects.all()
        if data.count():
            return JsonResponse({'students':list(data.values())})
        return JsonResponse({'Error':'not students available'})
        pass

    def post(self,request):
        try:
            form = StudentF(data = json.loads(request.body))
            if form.is_valid():
                form.save()
                return JsonResponse({'Message':'student added succesfully'})
            return JsonResponse(form.errors)
        except:
            return JsonResponse({'Error':'student data not valid'})
# :)
class StudentID(View): 
    def get(self,request,*args, **kwargs):
        data = Student.objects.filter(id=kwargs['id'])
        return JsonResponse({'student':data})

    def put(self,request,*args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
            form = StudentF(data=json.loads(request.body),instance=student)
            if(form.is_valid()):
                form.save()
                return JsonResponse({'Message':'student updated succesfully'})
            return JsonResponse(form.errors)
        except:
            return JsonResponse({'Error':'student data not valid'})

    def delete(self,request,*args, **kwargs):
        Student.objects.get(id=kwargs['id']).delete()
        return JsonResponse({'message':'Student deleted successfully'})