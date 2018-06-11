from django.db import models
import datetime
from uuid import uuid4

def create_id():
    now = datetime.datetime.now()
    return ('KIND_' + str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7])


class Kind_Company(models.Model):
    id_kind = models.CharField(primary_key=True,max_length=100,default=create_id, editable=False)
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
