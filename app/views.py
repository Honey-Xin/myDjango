from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth.models import User
from app.models import *
# Create your views here.


def get_index(request):
    return render(request,'index.html')

def to(request):
    return render(request,'test.html')

# 类视图---登录模板
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        lname = request.POST.get("lname")
        lpasswd = request.POST.get("lpassword")

        # 登录失败时需要提示是用户名不存在还是密码错误
        try:  # 存放可能出现异常的代码 查询数据多个条件时默认是并且的关系
            user = User.objects.get(username=lname)
            # 当输入的用户名在数据库里查询不到，说明try里面的代码存在异常
            # 执行万能异常里面的语句
        except Exception as e:  # 捕获异常将异常存到e里
            print(e)
            return HttpResponse("用户名不存在")

        # 如果用户名对，就判断密码有没有输入正确
        if lpasswd != user.password:
            return HttpResponse("用户名和密码不匹配")

        return render(request,'main.html',{"username":user})

class RegisterView(View):
    def get(self,request):
        return render(request, 'register.html')

    def post(self, request):
        rname = request.POST.get("email")
        rpasswd = request.POST.get("pwd1")

        # 注册成功跳转到到登录页面，注册加判断已经存在提示改用用户已存在
        users = User.objects.all()
        for i in users:
            if rname == i.username:
                return HttpResponse("用户已存在")
        try:
            User.objects.create(username=rname, password=rpasswd)
        except Exception as e:
            print(e)
            return HttpResponse("注册失败")
        return redirect('logined')

from app.cope import goON
#处理模块
def DoModify(request):
    pass
