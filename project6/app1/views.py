from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse('hello everyone,welcome to my world !')

# URL路径参数
def fun1(request,cat_id,detail_id):
    return HttpResponse('这是%s和%s!'%(cat_id,detail_id))

# Query String请求字符
def fun2(request):
    query_str = request.GET
    a = query_str.get('a')
    b = query_str.getlist('b')
    c = query_str.get('c','这是默认值')
    print(a)
    print(b)
    print(c)
    return HttpResponse('这是请求字符a=%s,b=%s,c=%s'%(a,b,c))
# 当get(key，xxx)或getlist(key，xxx)中的key不存在时将使用默认值xxx

# 表单类型数据的post请求
def fun3(request):
    body = request.POST
    return HttpResponse('{}'.format(body))

# Non-Form Data的post请求
def fun4(request):
    body = request.body
    print(body)
    body_str = body.decode()
    print(body_str)
    import json
    body_dic = json.loads(body_str)
    return HttpResponse('body=%s,body_str=%s,body_dic=%s'%(body,body_str,body_dic))