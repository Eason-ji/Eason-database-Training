from django.shortcuts import render,redirect
from django.http import HttpResponse

def ibd(request):
    return redirect("http://www.baidu.com")

def index(request):
    dic = {'variable':'你好呀'}
    return render(request,'app1/index.html',dic)


# Create your views here.
