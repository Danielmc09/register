from rest_framework import serializers
from EmployeeApp.models import Departement, Employees


class DeparmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ('DeparmentId', 'DeparmentName')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = ('EmployeeId', 'EmployeeName', 'Department', 'DateOfJoining', 'PhotoFileName')
