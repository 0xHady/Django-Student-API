from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics,status
from .serializers import *
from .models import *

# Create your views here.

def StudentV(APIView):
    def get(self,request):
        pass
    def post(self,request):
        pass

def StudentID(APIView):
    def get(self,request,*args, **kwargs):
        pass

    def put(self,request,*args, **kwargs):
        pass

    def delete(self,request,*args, **kwargs):
        pass