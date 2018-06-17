from django.urls import path
from django.contrib import admin
from .views import ListKindsCompanies,ViewKindsCompaneis

urlpatterns = [
    path('', ListKindsCompanies.as_view()),
    path('<str:pk>',ViewKindsCompaneis.as_view())
    ]