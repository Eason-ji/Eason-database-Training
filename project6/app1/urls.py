from django.urls import path
from app1 import views

urlpatterns = [
    path('index/',views.index),
    path('<cat_id>/<detail_id>/',views.fun1),
    path('func2/',views.fun2),
    path('func3/',views.fun3),
    path('func4/',views.fun4)

]