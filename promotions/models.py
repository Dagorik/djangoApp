from django.db import models
import datetime
from uuid import uuid4
from companies.models import Company

def create_id():
    now = datetime.datetime.now()
    return ('PROMOTION_' + str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7])


class Promotions(models.Model):
    id_promotion = models.CharField(primary_key=True,max_length=100,default=create_id, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_promotion
