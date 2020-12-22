from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'title':'1测试1,这是index'}
    return render(request,'app1/index.html',context)

def aa(request):
    return HttpResponse('这个是aa')