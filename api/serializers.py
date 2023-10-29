from rest_framework import serializers
from api.models import Company,Employee

class ComanySerializers(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        lookup_field = 'employees_id'
        fields = "__all__"


