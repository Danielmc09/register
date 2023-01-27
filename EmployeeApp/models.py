from django.db import models


# Create your models here.

class Departement(models.Model):
    DeparmentId = models.AutoField(primary_key=True)
    DeparmentName = models.CharField(max_length=500)


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateOfJoining = models.DateField(auto_now_add=True)
    PhotoFileName = models.CharField(max_length=500)

    def guardar_fecha(self):
        self.DateOfJoining = datetime.now()
        self.save()

    def retornar_fecha(self):
        return self.DateOfJoining
