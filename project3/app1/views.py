from django.shortcuts import render,redirect
def index(request):
    data = {'data':1111111111111111111111111111111111101010101010101010010100101010100101010001010101010}
    return render(request,'app1/index.html',data)
# Create your views here.

def bd(request):
    return redirect('http://www.baidu.com')
