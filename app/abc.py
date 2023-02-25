import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myDjango.settings")### 把test02 改成自己的项目名即可
django.setup()
from django.contrib.auth.models import User
from app.models import *
user = User.objects.get(username="1355885920@qq.com")
name = 0
atr = arTicle.objects.filter(user_id=user.id,arTicle_name=name)
print(user.password)