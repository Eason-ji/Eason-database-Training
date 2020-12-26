from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello everyone welcome to my world')

def html(request):
    data = {
        'data':'点我啊，使劲点我啊！'
    }
    return render(request,'app1/ht1.html',data)

# URL路径参数获取数据
def func1(request,cat_id,detail_id):
    return  HttpResponse('这是%s和%s'%(cat_id,detail_id))

# URL query_string参数获取值
def func2(request):
    query_string = request.GET
    print(query_string)
    a = query_string.get('a')
    b = query_string.getlist('b')
    c = query_string.get('c',"100")

    print(a,'\n',b,'\n',c)
    return HttpResponse('a=%s,b=%s,c=%s'%(a,b,c,))

# POST请求
# form data接受
def func3(request):
    query_str = request.POST
    print(query_str)
    return HttpResponse("%s"%query_str)

# Non-Form data接受
def func4(request):
    body = request.body
    print(body)
    body_str = body.decode()
    print(body_str)
    import json
    body_dic = json.loads(body_str)
    print(body_dic)

    return HttpResponse('body=%s,body_str=%s,body_dic=%s'%(body,body_str,body_dic))


"""----------数据库的使用---------------"""
from app1.models import BookInfo,PersonInfo
# ------------------增加数据-------------------
BookInfo.objects.create(name='Ｏ(≧口≦)Ｏ')
# ------------------修改数据-------------------
BookInfo.objects.filter(id=1).update(name='三国志')
# ------------------删除数据-------------------
BookInfo.objects.filter(id=5).delete()
# ------------------获取数据-------------------
BookInfo.objects.all() # 获取所有数据

# 过滤查询
BookInfo.objects.filter(name__contains='三') # 查询满足括号条件的值filter(属性名__运算方式=值) gt> gte>= lt< lte<=
BookInfo.objects.get(id=1)
BookInfo.objects.exclude(name__contains='三') # 除了满足括号里条件的值以外的值

# F对象
from django.db.models import F
BookInfo.objects.filter(name__contains=F(name='')) # 两个属性之间的判断

# Q对象
from django.db.models import Q
BookInfo.objects.filter(Q()&Q())  # & = and
BookInfo.objects.filter(Q()|Q())  # | = or
BookInfo.objects.filter(~Q())     # ~ = not

# 聚合函数
from django.db.models import Max,Min,Avg,Sum,Count
BookInfo.objects.aggregate(sum('name'))

# 排序
BookInfo.objects.all().order_by('name') #正序   反序为-name

# 关联查询
BookInfo.objects.get(id=1).personinfo_set.all()
# 过滤查询：BookInfo.objects.filter(personinfo__name__exact='关羽')    BookInfo.objects.filter(关联类名小写__关联类属性__exact='关联类属性值')
PersonInfo.objects.get(id=1).book
# 过滤查询：PersonInfo.objects.filter(book__name__exact='三国演义')     BookInfo.objects.filter(外键__关联类属性__exact='关联类属性值')

# 分页
from django.core.paginator import Paginator
# book = BookInfo.objects.all().order_by('id')
# 创建分页 pa = Paginator(object_list=book,per_page=2)
# 获取分页 pa_book = pa.page(2).object_list
# 获取分页总数 pa.num_pages

