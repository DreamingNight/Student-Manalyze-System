from django.contrib import admin

# Register your models here.


from stu_manage.models import Course
from stu_manage.models import Student
from stu_manage.models import Score

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Score)