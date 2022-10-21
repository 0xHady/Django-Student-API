from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import utility
import json


def get(request):
    return JsonResponse(data = utility.read_file('student/db.json'), safe = False)

def get_with_id(request ,id):
    students = utility.read_file('student/db.json')
    for i in range(len(students)):
        if students[i]['id'] == id:
            return JsonResponse(data = students[i], safe = False)
    return JsonResponse({"Error": 'Student id not found'},status = 404)

def post(request):
    pass

def put(request):
    pass

def delete(request):
    pass

def get_or_post(request):
    if(request.method == 'GET'):
        return get(request)
    return post(request)

def get_or_put_or_delete(request, id):
    if(request.method == 'PUT'):
        return put(request, id)
    elif(request.method == 'DELETE'):
        return delete(request, id)
    return get_with_id(request, id)