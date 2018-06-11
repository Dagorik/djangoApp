from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from .serializer import KindCompanySerializer
from .models import Kind_Company

class ListKindsCompanies(APIView):
    def get(self,request):
        kind_company = Kind_Company.objects.all()
        serializer = KindCompanySerializer(kind_company, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
