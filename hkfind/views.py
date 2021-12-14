from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import pymongo
import certifi
from pymongo import MongoClient
import dns
import json  
from django.core.serializers.json import DjangoJSONEncoder
from bson import BSON
from bson import json_util
from bson import objectid
from bson.json_util import dumps, loads

colle1 ='procesarcompras'
colle2 ='procesarcompraconsumables'
colle3 ='procesarupdateavatars'
URI_HK = "mongodb+srv://support:onqx7jk5j8tGzYNx@cluster0.trqu4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGODB_DATABASE = "myFirstDatabase"
MONGODB_TIMEOUT =100000



class MongoAwareEncoder(DjangoJSONEncoder):
    """JSON encoder class that adds support for Mongo objectids."""
    def default(self, o):
        if isinstance(o, objectid.ObjectId):
            return str(o)
        else:
            return super(MongoAwareEncoder, self).default(o)

#Home
def home(request):
 a = request.GET.get('hkfinder')
 if  a:
        client = conectar_Db()
        elresultado= procesando(client,colle1,a)
        if elresultado == 0:
             elresultado1= procesando(client,colle2,a)
             if elresultado1 == 0:
                  elresultado2= procesando(client,colle3,a)
                  if elresultado2 ==0:
                    nofounds="results : no found"
                    return  render(request,'hkfind/home.html', {"curso" : nofounds} )
                  else:
                   return render(request,'hkfind/home.html', {"curso" : elresultado2} )       
             else:
                 return render(request,'hkfind/home.html', {"curso" : elresultado1} )
             
        else:
         return render(request,'hkfind/home.html', {"curso" : elresultado } )
         
 else:
     return render(request, 'hkfind/home.html')



def procesando(client,destino,trx):
        destination = destino
        collection = client[MONGODB_DATABASE][destination]
        condition = {"trxid": trx}
        contador = collection.count_documents(condition)
        if contador == 0:
         return(0)
        else:
         result = collection.find_one(condition)
         thejson = json.dumps({'results':result}, cls=MongoAwareEncoder)
         return (thejson) 






def hksearch(request):
 pass
 


def conectar_Db():
  try:
    client = pymongo.MongoClient(URI_HK, serverSelectionTimeoutMS=MONGODB_TIMEOUT, maxPoolSize=10 , tlsCAFile=certifi.where()) 
    
  except pymongo.errors.ServerSelectionTimeoutError as error:
                print ('Error with mongoDB connection: %s' % error)
 #except pymongo.errors.ConnectionFailure as error:
                print ('Could not connect to MongoDB: %s' % error)
  return (client)        
