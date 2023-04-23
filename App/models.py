# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=9999)

    class Meta:
        managed = False
        db_table = 'administrator'


class Class(models.Model):
    course = models.OneToOneField('Course', models.DO_NOTHING, primary_key=True)  # The composite primary key (course_id, class_id, semester_id) found, that is not supported. The first column is selected.
    class_id = models.IntegerField()
    semester = models.ForeignKey('Semester', models.DO_NOTHING)
    teacher_id = models.IntegerField()
    classroom = models.CharField(max_length=100, blank=True, null=True)
    time = models.CharField(max_length=100, blank=True, null=True)
    current_selection = models.IntegerField(blank=True, null=True)
    max_selection = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'class'
        unique_together = (('course', 'class_id', 'semester'),)


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gp_percentage = models.FloatField(blank=True, null=True, db_comment='General Performance Percentage')
    dept = models.ForeignKey('Department', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class CourseSelection(models.Model):
    student = models.OneToOneField('Student', models.DO_NOTHING, primary_key=True)  # The composite primary key (student_id, course_id, class_id, semester_id) found, that is not supported. The first column is selected.
    course = models.ForeignKey(Class, models.DO_NOTHING)
    class_field = models.ForeignKey(Class, models.DO_NOTHING, db_column='class_id', to_field='class_id', related_name='courseselection_class_field_set')  # Field renamed because it was a Python reserved word.
    semester = models.ForeignKey(Class, models.DO_NOTHING, to_field='semester_id', related_name='courseselection_semester_set')
    gp = models.FloatField(blank=True, null=True, db_comment='General Performance')
    exam = models.FloatField(blank=True, null=True)
    grade = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course_selection'
        unique_together = (('student', 'course', 'class_field', 'semester'),)


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
    major = models.OneToOneField(Major, models.DO_NOTHING, primary_key=True)  # The composite primary key (major_id, course_id) found, that is not supported. The first column is selected.
    course = models.ForeignKey(Course, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'major_plan'
        unique_together = (('major', 'course'),)


class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'semester'


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    password = models.CharField(max_length=9999)
    gpa = models.FloatField(db_column='GPA', blank=True, null=True)  # Field name made lowercase.
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    major = models.ForeignKey(Major, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'student'


class Teacher(models.Model):
    teacher_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    dept = models.ForeignKey(Department, models.DO_NOTHING)
    password = models.CharField(max_length=9999)

    class Meta:
        managed = False
        db_table = 'teacher'
