from django.urls import path
from django.contrib import admin
from .views import ListPromotions

urlpatterns = [
    path('', ListPromotions.as_view())
    
    ]