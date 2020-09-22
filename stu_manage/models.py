from django.db import models

# Create your models here.
# 三个表


class Score(models.Model):
    stu_id = models.ForeignKey('Student', on_delete=models.CASCADE)
    course_id = models.ForeignKey('Course', on_delete=models.CASCADE)
    score = models.IntegerField(verbose_name='分数')

    def __str__(self):
        return str(self.score)

    class Meta:
        verbose_name = '成绩'
        verbose_name_plural = '成绩'


class Student(models.Model):
    stu_id = models.IntegerField(primary_key=True, verbose_name='学号')
    stu_name = models.CharField(max_length=20, verbose_name='学生姓名')
    MALE = 'MALE'
    FEMALE = 'FEMALE'
    GENDER_CHOICE = ((MALE, '男'), (FEMALE, '女'))
    stu_gender = models.CharField(max_length=10, choices=GENDER_CHOICE, verbose_name='性别')
    
    stu_grade = models.CharField
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stu_id) + self.stu_name

    class Meta:
        verbose_name = '学生名单'
        verbose_name_plural = '学生名单'


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=5, verbose_name='科目')

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = '历次考试科目'
        verbose_name_plural = '历次考试科目'
