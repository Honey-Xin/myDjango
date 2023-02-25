from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class auThor(models.Model):
    # author_id = models.AutoField(primary_key=True,unique=True,verbose_name="作者ID")
    # author_id = models.IntegerField('作者ID',max_length=11,null=False)
    auThor_name = models.CharField('姓名',max_length=255)
    auThor_sex = models.CharField('性别',max_length=20)
    auThor_birthy = models.CharField('出生年月',max_length=255,null=True)
    auThor_phone = models.IntegerField('联系方式',max_length=11,null=True)

    user = models.ForeignKey(to=User,on_delete=models.CASCADE,null=True)


class arTicle(models.Model):
    # arTicle_id = models.AutoField(primary_key=True,unique=True,verbose_name='剧本ID')
    # arTicle_id = models.IntegerField('剧本ID',max_length=11,null=False)
    arTicle_name = models.CharField('剧本名',max_length= 255,null=True)
    arTicle_theme = models.CharField('剧本主题',max_length=255,null=True)
    arTicle_content = models.CharField('剧本内容',max_length=10000,null=False)
    arTicle_score = models.IntegerField('剧本得分',max_length=11,null=True)
    arTicle_auThor_id = models.ForeignKey(to=auThor,on_delete=models.CASCADE,null=True) # 关联