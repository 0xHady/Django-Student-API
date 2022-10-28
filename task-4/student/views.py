from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins,generics,status
from .serializers import *
from .models import *
from django.http import JsonResponse

# Create your views here.
class StudentV(APIView):
    def get(self,request):
        data = StudentSerializer(Student.objects.all())
        return Response(data.data)

    def post(self,request):
            serializer = StudentSerializer(data=request.data)
            if(serializer.is_valid()):
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

class StudentID(APIView):
    def get(self,request,*args, **kwargs):
        try:
            serializer = StudentSerializer(Student.objects.get(id=kwargs['id']))
            return Response(serializer.data)
        except:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self,request,*args, **kwargs):
        serializer = StudentSerializer(data=request.data,
        instance=Student.objects.get(id=kwargs['id']))
        
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self,request,*args, **kwargs):
        try:
            student = Student.objects.get(id=kwargs['id'])
            student.delete()
            return Response(status.HTTP_200_OK)
        except:
            return Response(status.HTTP_404_NOT_FOUND)
