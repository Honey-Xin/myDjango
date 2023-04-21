import requests
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from app.models import *
from app.cope import util
# Create your views here.
'''
测试上传
'''

def get_index(request):
    '''
    访问网站起始页
    '''
    return render(request,'index.html')

def to(request):
    '''
    访问网站主页，判断session
    '''
    if 'username' in request.session:
        username = request.session['username']
        return render(request, 'test.html', {"username": username})
    return render(request, 'login.html')

# 类视图---登录模板
class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        lname = request.POST.get("lname")
        lpasswd = request.POST.get("lpassword")

        # 登录失败时需要提示是用户名不存在还是密码错误
        try:
            user = User.objects.get(username=lname)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=lname)

            except User.DoesNotExist:
                return HttpResponse("用户名不存在")

        # 如果用户名对，就判断密码有没有输入正确
        if lpasswd != user.password:
            return HttpResponse("用户名和密码不匹配")
        a = user.username
        #保存作者id用于后续表查询
        request.session['username'] = user.username
        request.session['userid'] = user.id
        userid = request.session['userid']
        author = auThor.objects.get(user_id=userid)
        request.session['authorid'] = author.auID

        return render(request,'test.html',{"username":user})

class RegisterView(View):
    def get(self,request):
        return render(request, 'register.html')

    def post(self, request):
        remail = request.POST.get("email")
        rpasswd = request.POST.get("pwd1")
        rname = request.POST.get('name')
        if not (remail and rpasswd and rname):
            return HttpResponse('信息未完善')

        # 注册成功跳转到到登录页面，注册加判断已经存在提示改用用户已存在
        users = User.objects.all()
        for i in users:
            if rname == i.username:
                return HttpResponse("用户已存在")
        try:
            user = User.objects.create(username=rname, password=rpasswd,email=remail)
            auThor.objects.create(user = user, name=rname)
        except Exception as e:
            print(e)
            return HttpResponse("注册失败")
        return redirect('logined')

#退出登录
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    request.session.clear()
    return redirect('logined') # redirect到登录页面

from app.cope import goON
#处理模块
def Dom(request):
    name = request.POST.get("name")
    text = request.POST.get("text")
    theme = request.POST.get("theme")
    # 处理内容,先存在数据库
    try:
        text = [i+'。' for i in text.split('。')]
        goON.texts.extend(text)
        result = goON.get_result()
        data = {"matches": []}
        pre_text_length = 0#前面句子的长度
        paper = []
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
            if res[0]!='。':
                paper.extend(res[0])
            pre_text_length += len(res[0])  # 前面句子的长度
        data['all'] = ''.join(paper)
        goON.texts = []
        return JsonResponse(data)
    except Exception as e:
        print(e)
        return HttpResponse("添加失败")
    return HttpResponse("测试")


# 解析文件
from django.conf import settings
import time,os
def upload(request):
    if request.method == 'POST' and request.FILES['file']:
        # 处理文件数据，如保存到服务器或进行其他操作
        myfile = request.FILES.get('file', None)
        try:
            suffix = str(myfile.name.split('.')[-1])  # 文件后缀
            times = str(time.time()).split('.').pop()  # 生成时间戳，取小数点后的值
            fil = str(myfile.name.split('.')[0])  # 文件名
            filename = times + '_' + fil + '.' + suffix  # 拼接文件名
            filename_dir = settings.MEDIA_ROOT  # 文件保存路径
            # 保存文件
            with open(filename_dir + filename, 'wb+') as destination:
                for chunk in myfile.chunks():
                    destination.write(chunk)
                destination.close()
            # 解析文件
            if suffix == 'docx':
                text = util.get_docx_text(filename_dir + filename)
            else:
                text = util.get_pdf_text(filename_dir + filename)
            data = {"textname":fil,
                    "textcontent":text
                    }
        except:
            return JsonResponse({'success': False, 'message': '上传失败'})

        return JsonResponse(data)
    else:
        return JsonResponse({'success': False, 'message': '上传失败'})

#保存信息
def save(request):
    text1 = request.POST.get('text1')
    text2 = request.POST.get('text2')
    name = request.POST.get('name')
    theme = request.POST.get('theme')
    auID = request.session['authorid']
    try:
        arTicle.objects.create(name=name,
                           theme=theme,
                           content1=text1,
                           content2=text2,
                           arTicle_auThor=auThor.objects.get(auID=auID)
                            )
    except Exception as e:
        return JsonResponse({'success': False, 'message': '上传失败'})

    return JsonResponse({'text1':text1,'text2':text2,'name':name,'theme':theme})


def user_info(request):
    userid = request.session['userid']
    # username = User.objects.get(pk=userid).
    user = auThor.objects.filter(user_id=userid)
    if not user.exists():
        print("No matching records found.")
    else:
        author = user.first()
    return render(request, 'info.html', {'username': request.session['username'],'author':author})
def upInfo(request):
    # name = request.POST.get('name')
    sex = request.POST.get('sex')
    phone = request.POST.get('phone')
    style = request.POST.get('style')
    info = request.POST.get('info')
    borth = request.POST.get('borth')
    author = auThor.objects.filter(user_id=request.session['userid'])
    try:
        author.update(sex=sex,phone=phone,style=style,info=info,birthy=borth)
    except Exception as e:
        return HttpResponse('保存失败')
    return redirect('info')

#用户历史文稿
def myDoc(request):
    return render(request,'mydoc.html')