"""myDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',get_index,name='index'),
    path('logout',logout_view,name='logout'),
    # path('register',register,name='register'),
    path('registered',RegisterView.as_view(),name='registered'),
    path('logined',LoginView.as_view(),name='logined'),
    path('test',to,name='test'),
    path('my',Dom, name='my'),
    path('upload',upload,name='upload'),
    path('save',save,name='save'),
    path('info',user_info,name='info'),
    path('upinfo',upInfo,name='upInfo'),
    path('mydoc',myDoc,name='mydoc'),
    path('detail/<str:pk>',detail_text,name='detail_text')
]
