# Generated by Django 3.1 on 2020-09-01 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.IntegerField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stu_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stu_name', models.CharField(max_length=20)),
                ('stu_gender', models.CharField(choices=[('MALE', '男'), ('FEMALE', '女')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu_manage.course')),
                ('stu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stu_manage.student')),
            ],
        ),
    ]