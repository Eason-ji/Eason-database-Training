from django.shortcuts import render,redirect

def app2_index(request):
    data = {'data':'1212131313'}
    render(request,"app2/app2_index.html",data)
# Create your views here.
