from django.contrib import admin

# Register your models here.


from stu_manage.models import Test
from stu_manage.models import Examination
from stu_manage.models import Student
from stu_manage.models import Score

admin.site.register(Test)
admin.site.register(Examination)
admin.site.register(Student)
admin.site.register(Score)