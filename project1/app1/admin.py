from django.contrib import admin
from app1.models import Book,Person
# Register your models here.
# 注册书籍模型
admin.site.register(Book)
# 注册人物模型
admin.site.register(Person)