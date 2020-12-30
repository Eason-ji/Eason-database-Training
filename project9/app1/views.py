from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# 创造一个视图函数
def index(request):
    return HttpResponse('这是index！！！！！！！！！！！！！！！！')



# 创建一个类视图
# View类可以判断接受的请求是POST还是GET
class center_1(View):
    # 判断是POST请求还是GET请求
    def post(self,request):
        return HttpResponse('this is post')

    def get(self,request):
        return HttpResponse('this is get')

# 使用多继承方式进行

# LoginRequiredMixin类只为帮助我们去判断客户端是否登录的一个类
# 如果未编辑accounts/login页面，也没有用户登录则会跳转失败
class center_2(LoginRequiredMixin,View):

    def post(self,request):
        return HttpResponse('this is post')

    def get(self,request):
        return HttpResponse('this is get')

