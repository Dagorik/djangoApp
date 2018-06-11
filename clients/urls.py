from django.urls import path
from django.contrib import admin
from .views import ListClients,ClientView

urlpatterns = [
    path('', ListClients.as_view()),
    path('<str:pk>',ClientView.as_view())
]