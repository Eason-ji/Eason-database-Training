from django.urls import path
from app1 import views

urlpatterns = [
    path('aa/',views.aa),
    path('index/',views.index)
]
