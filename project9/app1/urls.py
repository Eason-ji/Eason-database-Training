from django.urls import path
from app1 import views

urlpatterns = [
    path('index/',views.index),
    path('center1/',views.center_1.as_view()),
    path('center2/',views.center_2.as_view())
]