from django.db import models
import datetime
from uuid import uuid4
from clients.models import Client
def create_id():
    now = datetime.datetime.now()
    return ('REPORT_' + str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7])


class Reports(models.Model):
    id_report = models.CharField(primary_key=True,max_length=100,default=create_id, editable=False)
    name = models.CharField(max_length=200)
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    date = models.CharField(max_length=200)
    lat = models.CharField(max_length=200)
    lon = models.CharField(max_length=200)
    type = models.CharField(max_length=200) #Agregar la regla de negecios para los numeros.
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    repair = models.IntegerField()
    
    def __str__(self):
        return self.name
