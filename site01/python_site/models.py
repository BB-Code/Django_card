from django.db import models
from mongoengine import *
#from site01.settings import DBNAME

connect('python')
# Create your models here.
class Articles_info(Document):
    title = StringField(max_length=100, required=True)
    url = StringField(max_length=100, required=True)
    date = StringField(max_length=30, required=True)

   

for i in Articles_info.objects:  # 测试是否连接成功
    print(i.title)

