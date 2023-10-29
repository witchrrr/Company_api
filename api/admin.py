from django.contrib import admin
from api.models import Company,Employee
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','location')
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','position')


admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)