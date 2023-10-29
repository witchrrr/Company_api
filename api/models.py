from django.db import models

# Create your models here.

#Creating Company Model 

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField(default=True)
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ("Mobiles Phones",'Mobile Phones')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name +'--'+ self.location
    
    
    
#Employee Model
class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50,default=False)
    phone=models.CharField(max_length=10,default=False)
    about=models.TextField(default=True)
    position=models.CharField(max_length=50,default=False,choices=(
        ('Manager','manager'),
        ('Software Developer','Software Developer'),
        ('Project Leader','Project Leader')
    ))
    
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
    
    