from django.db import models
import datetime
from uuid import uuid4
from kinds_companies.models import Kind_Company

def create_id():
    now = datetime.datetime.now()
    return ('COMPANY_' + str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7])


class Company(models.Model):
    id_company = models.CharField(primary_key=True,max_length=100,default=create_id, editable=False)
    name = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    lat = models.CharField(max_length=200,null= True)
    lon = models.CharField(max_length=200,null= True)
    service_hour = models.CharField(max_length=200,null= True)
    type_company = models.ForeignKey(Kind_Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_company
