# Generated by Django 4.2 on 2023-05-05 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0014_remove_student_major_delete_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseselection',
            name='gpa',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
