from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from .serializer import CompanySerializer
from .models import Company

class ListCompanies(APIView):
    def get(self,request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(slef,request):
        serializer = CompanySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyView(APIView):
    def _getCompany(self,pk):
        try:
            return Company.objects.get(id_company = pk)
        except:
            raise Http404
    
    def get(self,request,pk):
        company = self._getCompany(pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self,request,pk):
        company = get_object_or_404(Company,pk = pk)
        company.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk):
        data = request.data
        company = Company.objects.get(id_company = pk)
        serializer = CompanySerializer(company,data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)