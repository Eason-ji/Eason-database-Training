from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('index/', views.index),
    path('ibd/',views.ibd)
]