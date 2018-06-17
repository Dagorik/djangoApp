from django.shortcuts import render,get_object_or_404
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status,generics, filters
from rest_framework.response import Response
from .serializer import PromotionSerializer
from .models import Promotions


class ListPromotions(APIView):
    def get(self,request):
        promotions = Promotions.objects.all()
        serializer = PromotionSerializer(promotions, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)



