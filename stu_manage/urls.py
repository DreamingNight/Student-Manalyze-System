# 定义在stu_manage应用程序中的URL模式

from django.conf.urls import url
from . import views

urlpatterns = [
    # 匹配基础主页
    url('^$', views.index, name='index'),
    url('^students/$', views.students, name='students'),
]
