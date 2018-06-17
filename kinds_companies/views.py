from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from .serializer import KindCompanySerializer
from .models import Kind_Company

from companies.models import Company
from companies.serializer import CompanySerializer

class ListKindsCompanies(APIView):
    def get(self,request):
        kind_company = Kind_Company.objects.all()
        serializer = KindCompanySerializer(kind_company, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ViewKindsCompaneis(APIView):
    def _getKindCompany(self,pk):
        try:
            return Kind_Company.objects.get(id_kind = pk)
        except:
            return Http404
    def _getCompanies(self,typeId):
        try :
            
            return Company.objects.all().filter(type_company = typeId)
        except:
            return Http404

    def get(self,request,pk):
        kind_company = self._getCompanies(pk)
        serializer = CompanySerializer(kind_company,many= True)
        return Response(serializer.data, status = status.HTTP_200_OK)

