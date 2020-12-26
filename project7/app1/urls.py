from django.urls import path
from app1 import views

urlpatterns = [
    path('index/',views.index),
    path('html',views.html),
    path('<cat_id>/<detail_id>',views.func1),
    path('fun2/',views.func2),
    path('func3/',views.func3),
    path('func4/',views.func4)
]