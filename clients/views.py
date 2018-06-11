from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from .serializer import ClientSerializer,DevicedIdSerializer
from .models import Client

class ListClients(APIView):

    def post(self,request):
        #device_id = request.data.get('device_id')
        #serialize_device = DevicedIdSerializer(data = request.data)
        serializer = ClientSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ClientView(APIView):
    def _getClient(slef,pk):
        try:
            return Client.objects.get(id_client=pk)
        except:
            return Http404
    
    def get(self,request,pk):
        client = self._getClient(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data, status.HTTP_200_OK)