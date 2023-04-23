# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrator'


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

    class Meta:
        managed = False
        db_table = 'class'


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gp_percentage = models.FloatField(blank=True, null=True, db_comment='General Performance Percentage')
    dept = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class CourseSelection(models.Model):
    course_selection_id = models.AutoField(primary_key=True)
    student = models.ForeignKey('Student', models.DO_NOTHING)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class_id')  # Field renamed because it was a Python reserved word.
    gp = models.FloatField(blank=True, null=True, db_comment='General Performance')
    exam = models.FloatField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_selection'


class Department(models.Model):
    dept_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=9999, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major'


class MajorPlan(models.Model):
    major_plan_id = models.AutoField(primary_key=True)
    major = models.ForeignKey(Major, models.DO_NOTHING)
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'major_plan'


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semester'


class Student(models.Model):
    student_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    gpa = models.FloatField(blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    major = models.ForeignKey(Major, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    teacher_id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'teacher'
