from app2 import views
from django.urls import path

urlpatterns = [
    path('app2_index',views.app2_index)
]