# Django
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.core.files.storage import default_storage

# RestFramework
from rest_framework.parsers import JSONParser

# Models and Serializers
from EmployeeApp.models import Departement, Employees
from EmployeeApp.serializers import DeparmentSerializer, EmployeeSerializer


# Create your views here.


@csrf_exempt
def deparmetnApi(request, id=0):
    if request.method == 'GET':
        deparment = Departement.objects.all()
        deparment_serializer = DeparmentSerializer(deparment, many=True)
        return JsonResponse(deparment_serializer.data, safe=False)
    elif request.method == 'POST':
        deparment_data = JSONParser().parse(request)
        deparment_serializer = DeparmentSerializer(data=deparment_data)
        if deparment_serializer.is_valid():
            deparment_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        deparment_data = JSONParser().parse(request)
        deparment = Departement.objects.get(DeparmentId=deparment_data['DeparmentId'])
        deparment_serializer = DeparmentSerializer(deparment, data=deparment_data)
        if deparment_serializer.is_valid():
            deparment_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        deparment = Departement.objects.get(DeparmentId=id)
        deparment.delete()
        return JsonResponse("Delete Successfully", safe=False)


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employee = Employees.objects.all()
        employee_serializer = EmployeeSerializer(employee, many=True)
        return JsonResponse(employee_serializer.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Delete Successfully", safe=False)


@csrf_exempt
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
