from django.db import models

# Create your models here.
# 四个表


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
    GRADE_CHOICE = (('1', '高一'), ('2', '高二'), ('3', '高三'))
    stu_grade = models.CharField(max_length=2, choices=GENDER_CHOICE, verbose_name='年级')

    
    # date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.stu_id) + self.stu_name

    class Meta:
        verbose_name = '学生名单'
        verbose_name_plural = '学生名单'


class Exam(models.Model):
    exam_name = models.CharField(max_length=15, verbose_name='考试名称')
    exam_date = models.DateField(verbose_name='考试日期')

    def __str__(self):
        return self.exam_name

    class Meta:
        verbose_name = '考试列表'
        verbose_name_plural = '考试列表'


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    exam_name = models.ForeignKey('Exam', on_delete=models.CASCADE)
    SUBJECT_CHOICE = (('1', '语文'), ('2','数学'), ('3','英语'), ('4','物理'), ('5','化学'), ('6','生物'), ('7','历史'), ('8','地理'), ('9','政治'))
    subject = models.CharField(max_length=2, choices=SUBJECT_CHOICE, verbose_name='科目')

    def __str__(self):
        return self.exam_name + self.subject

    class Meta:
        verbose_name = '考试科目'
        verbose_name_plural = '考试科目'
