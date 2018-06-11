from django.db import models
import datetime
from uuid import uuid4

def create_id():
    now = datetime.datetime.now()
    return ('CLIENT_' + str(now.year)+str(now.month)+str(now.day)+str(uuid4())[:7])


class Client(models.Model):
    id_client = models.CharField(primary_key=True,max_length=200)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.id_client
