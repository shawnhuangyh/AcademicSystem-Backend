from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    admin_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)


class Class(models.Model):
    class_id = models.AutoField(primary_key=True)
    course = models.ForeignKey('Course', models.DO_NOTHING)
    class_no = models.IntegerField()
    semester = models.ForeignKey('Semester', models.DO_NOTHING)
    teacher = models.ForeignKey('Teacher', models.DO_NOTHING)
    classroom = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    current_selection = models.IntegerField(blank=True, null=True)
    max_selection = models.IntegerField(blank=True, null=True)


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gp_percentage = models.FloatField(blank=True, null=True, db_comment='General Performance Percentage')
    dept = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)


class CourseSelection(models.Model):
    course_selection_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    class_field = models.ForeignKey(Class, models.DO_NOTHING,
                                    db_column='class_id')  # Field renamed because it was a Python reserved word.
    gp = models.FloatField(blank=True, null=True, db_comment='General Performance')
    exam = models.FloatField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=9999, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)


class MajorPlan(models.Model):
    major_plan_id = models.AutoField(primary_key=True)
    major = models.ForeignKey(Major, models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    major = models.ForeignKey(Major, models.DO_NOTHING)


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
