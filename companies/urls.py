from django.urls import path
from django.contrib import admin
from .views import ListCompanies,CompanyView

urlpatterns = [
    path('', ListCompanies.as_view()),
    path('<str:pk>',CompanyView.as_view())
]