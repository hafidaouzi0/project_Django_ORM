from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    
   path('home/',views.Home)
]