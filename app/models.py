from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class auThor(models.Model):
    # auID = models.AutoField(primary_key=True,auto_created=True,default=1)
    name = models.CharField('用户名',max_length=255,default='none')
    sex = models.CharField('性别',max_length=20,default='none')
    birthy = models.CharField('出生年月',max_length=255,default='none',null=True)
    phone = models.CharField('联系方式',max_length=11,default='none',null=True)
    info = models.CharField('简介',max_length=1000,default='none',null=True)
    style = models.CharField('写作风格',max_length=1000,default='none',null=True)
    user = models.ForeignKey(to=User,on_delete=models.CASCADE,to_field="id",null=False,default=-1)


class arTicle(models.Model):
    # arID = models.AutoField('剧本ID',auto_created=True,primary_key=True,default=1)
    name = models.CharField('剧本名称',max_length= 255,default='none',null=True)
    theme = models.CharField('文稿类型',max_length=255,default='none',null=True)
    content1 = models.CharField('剧本内容1',max_length=10000,default='none',null=True)
    content2 = models.CharField('剧本内容2', max_length=10000,default='none', null=True)

    arTicle_auThor = models.ForeignKey(to=auThor,on_delete=models.CASCADE,to_field="id",null=False,default=-1) # 关联

#保存上传文件
# class MyFile(models.Model):
#     my_file = models.FileField(upload_to='upload/')


