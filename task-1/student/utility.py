from django.http import JsonResponse
import json

def read_file(file):
    with open(file,'r') as temp:
        return json.load(temp,strict=False)

def write_file(file,data):
    with open(file,'w') as temp:
        json.dump(data,temp)