from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt # to let access other domain to access our api
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from rep_app.models import Company, User, Device
from rep_app.serializers import CompanySerializer, UserSerializer, DeviceSerializer

@csrf_exempt
def company_api(request, id=0):
    
    if request.method == 'GET':
        
        # if id == 0:
        #     companies = Company.objects.all()
        #     companies_serializer = CompanySerializer(companies, many = True)
        #     return JsonResponse(companies_serializer.data, safe = False)
        
        # else:
        #     company = Company.objects.get(com_id = id)
        #     company_serializer = CompanySerializer(company, many = True)
        #     return JsonResponse(company_serializer.data, safe = False)
        companies = Company.objects.all()
        companies_serializer = CompanySerializer(companies, many = True)
        return JsonResponse(companies_serializer.data, safe = False)
    
    elif request.method == 'POST':
        company_data = JSONParser().parse(request)
        company_serializer = CompanySerializer(data = company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed", safe = False)
    
    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company_id_data = Company.objects.get(com_id = company_data['com_id'])
        company_serializer = CompanySerializer(company_id_data, data = company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed", safe = False)
    
    elif request.method == 'DELETE':
        company = Company.objects.get(com_id = id)
        company.delete()
        return JsonResponse("Deleted", safe=False)
    

@csrf_exempt
def user_api(request, id=0):

    if request.method == 'GET':
        
        if id == 0:
            users = User.objects.all()
            users_serializer = UserSerializer(users, many = True)
            return JsonResponse(users_serializer.data, safe = False)
        
        else:
            user = User.objects.get(com_id = id)
            user_serializer = UserSerializer(user, many = True)
            return JsonResponse(user_serializer.data, safe = False)
        
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed", safe = False)
    
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_id_data = User.objects.get(com_id = user_data['user_id'])
        user_serializer = CompanySerializer(user_id_data, data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed", safe = False)
    
    elif request.method == 'DELETE':
        user = User.objects.get(user_id = id)
        user.delete()
        return JsonResponse("Deleted", safe=False)


@csrf_exempt
def device_api(request, id=0):

    if request.method == 'GET':
        
        if id == 0:
            devices = Device.objects.all()
            device_serializer = DeviceSerializer(devices, many = True)
            return JsonResponse(device_serializer.data, safe = False)
        
        else:
            device = Device.objects.get(com_id = id)
            device_serializer = DeviceSerializer(device, many = True)
            return JsonResponse(device_serializer.data, safe = False)       
    
    elif request.method == 'POST':
        device_data = JSONParser().parse(request)
        device_serializer = DeviceSerializer(data = device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse("Added Successfully", safe = False)
        return JsonResponse("Failed", safe = False)
    
    elif request.method == 'PUT':
        device_data = JSONParser().parse(request)
        device_id_data = Device.objects.get(com_id = device_data['device_id'])
        device_serializer = DeviceSerializer(device_id_data, data = device_data)
        if device_serializer.is_valid():
            device_serializer.save()
            return JsonResponse("Updated Successfully", safe = False)
        return JsonResponse("Failed", safe = False)
    
    elif request.method == 'DELETE':
        device = Device.objects.get(device_id = id)
        device.delete()
        return JsonResponse("Deleted", safe=False) 
    

        





