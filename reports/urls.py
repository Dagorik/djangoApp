from django.urls import path
from django.contrib import admin
from .views import ListReports,ViewReports

urlpatterns = [
    path('', ListReports.as_view()),
    path('<str:pk>',ViewReports.as_view())
]