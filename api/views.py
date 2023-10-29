from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from api.models import Company,Employee
from api.serializers import ComanySerializers,EmployeeSerializer   
from rest_framework.response import Response

# Create your views here.

class CompanyViewSets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = ComanySerializers
    # companies/{company_id}/employess
    @action(detail=True,methods = ['get'])
    def employees(self,request,pk = None):
        try:
            company = Company.objects.get(pk=pk)
            emps =Employee.objects.filter(company=company)
            emps_serializers = EmployeeSerializer(emps ,many = True ,context = {'request': request})
            return Response(emps_serializers.data )
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })
        

class EmployeeViewSets(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
