from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from .models import Student, Parent, Subject
import json

# Create your views here.

class StudentV(View):
    def get(request,*args, **kwargs):
        return HttpResponse("hello world")

    pass

class StudentID(View):
    pass