from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from app.models import *
from app.cope import *
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

        return render(request,'test.html',{"username":user})

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
def Dom(request):
    name = request.POST.get("name")
    text = request.POST.get("text")
    theme = request.POST.get("theme")
    # 处理内容,先存在数据库
    try:
        user = User.objects.get(username="1355885920@qq.com")
        # arTicle.objects.create(arTicle_name=name,
        #                       arTicle_theme=theme,
        #                       arTicle_content=text,
        #                       arTicle_score=0,
        #                       arTicle_auThor_id=user)
        text = [i+'。' for i in text.split('。')]
        goON.texts.extend(text)
        result = goON.get_result()
        data = {"matches": []}
        pre_text_length = 0#前面句子的长度
        for res in result:#返回的纠错信息
            for item in res[1]:#纠错信息详情
                #设置信息
                data_item = {
                    "message": item[0],#错误字段
                    "short_message": "Uppercase",
                    "offset":  pre_text_length+item[2],#错误位置
                    "length": len(item[1])+4,#错误长度
                    "context": {
                        "text": item[1],#正确文字
                        "offset": item[2]+4
                    },
                    "replacements": [
                        item[1]#替换的文字
                    ],
                }
                data["matches"].append(data_item)
            pre_text_length += len(res[0])  # 前面句子的长度

        return JsonResponse(data)
    except Exception as e:
        print(e)
        return HttpResponse("添加失败")
    return HttpResponse("测试")

