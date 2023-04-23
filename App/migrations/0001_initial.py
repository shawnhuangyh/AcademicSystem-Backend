# Generated by Django 4.2 on 2023-04-23 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('admin_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=9999)),
            ],
            options={
                'db_table': 'administrator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_no', models.IntegerField()),
                ('classroom', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('current_selection', models.IntegerField(blank=True, null=True)),
                ('max_selection', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('gp_percentage', models.FloatField(blank=True, db_comment='General Performance Percentage', null=True)),
            ],
            options={
                'db_table': 'course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CourseSelection',
            fields=[
                ('course_selection_id', models.AutoField(primary_key=True, serialize=False)),
                ('gp', models.FloatField(blank=True, db_comment='General Performance', null=True)),
                ('exam', models.FloatField(blank=True, null=True)),
                ('grade', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'course_selection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=9999, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Major',
            fields=[
                ('major_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'major',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MajorPlan',
            fields=[
                ('major_plan_id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'major_plan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'semester',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=9999)),
                ('gpa', models.FloatField(blank=True, db_column='GPA', null=True)),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(max_length=9999)),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
    ]