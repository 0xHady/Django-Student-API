from turtle import st
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import utility
import json

db_json_file = 'student/db.json'

def get(request):
    return JsonResponse(data = utility.read_file(db_json_file), safe = False)

def get_with_id(request ,id):
    students = utility.read_file(db_json_file)
    for i in range(len(students)):
        if students[i]['id'] == id:
            return JsonResponse(data = students[i], safe = False)
    return JsonResponse({"Error": 'Student id not found'},status = 404)

def post(request):
    students = utility.read_file(db_json_file)
    data = json.loads(request.body.decode('utf-8'), strict = False)
    students.append(data)
    utility.write_file(db_json_file,students)
    return JsonResponse(data = request.body.decode('utf-8'), safe = False)

def put(request, id):
    students = utility.read_file(db_json_file)
    for i in range(len(students)):
        if(students[i]['id'] == id):
            students[i] = json.loads(request.body,strict=False)
            utility.write_file(db_json_file,students)
            return JsonResponse({"message": "Updated succesfully"},status = 200)
    return JsonResponse({"Error": "Student id not found"},status = 404)

def delete(request, id):
    students = utility.read_file(db_json_file)
    for i in range (len(students)):
        if(students[i]['id'] == id):
            students.pop(i)
            utility.write_file(db_json_file,students)
            return JsonResponse({"message": "Deleted succesfully"},status = 200)
    return JsonResponse({"Error": "Student id not found"},status = 404)

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