from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from .serializer import ReportsSerializer
from .models import Reports

class ListReports(APIView):
    def get(self,request):
        reports = Reports.objects.all()
        serializer = ReportsSerializer(reports, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ReportsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)

class ViewReports(APIView):
    def _getReport(self,pk):
        try:
            return Reports.objects.get(id_report = pk)
        except:
            raise Http404
    
    def get(self,request,pk):
        report = self._getReport(pk)
        serializer = ReportsSerializer(report)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def delete(self,request,pk):
        report = get_object_or_404(Reports,pk = pk)
        report.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

    def patch(self,request,pk):
        data = request.data
        report = Reports.objects.get(id_report = pk)
        serializer = ReportsSerializer(report,data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)