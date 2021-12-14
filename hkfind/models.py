# Create your models here.
#from django.db import models

from djongo import models


# Create your models here.
class Usuarios(models.Model): 
   nombre=models.CharField(max_length=80)
   edad=models.FloatField()
   objects=models.DjongoManager()
   
  
class Consumables(models.Model):
 _id = models.ObjectIdField()
trxid=models.CharField(max_length=200)
username=models.CharField(max_length=200)
consumable=models.CharField(max_length=200)
token_amount=models.CharField(max_length=200)
token=models.CharField(max_length=200)
status=models.CharField(max_length=200)


class Procesarcompras(models.Model):
 trxid=models.CharField(max_length=200)
 username=models.CharField(max_length=200)
 consumable=models.CharField(max_length=200)
 token_amount=models.CharField(max_length=200)
 token=models.CharField(max_length=200)
 status=models.CharField(max_length=200)
