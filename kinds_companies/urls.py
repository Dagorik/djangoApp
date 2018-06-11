from django.urls import path
from django.contrib import admin
from .views import ListKindsCompanies

urlpatterns = [
    path('', ListKindsCompanies.as_view())]