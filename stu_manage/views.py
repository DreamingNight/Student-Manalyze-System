from django.shortcuts import render

# Create your views here.
from .models import Student


def index(request):
    # 主页
    return render(request, 'stu_manage/index.html')


def students(request):
    # 显示学生名单
    stu = Student.objects.order_by('stu_id')
    context = {'stu': stu}
    return render(request, 'stu_manage/students.html', context)
