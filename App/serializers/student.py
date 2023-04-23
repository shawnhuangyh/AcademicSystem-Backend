from rest_framework import serializers

from App.models import Student


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'name',
            'gpa',
            'dept_id',
            'major_id',
        ]


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            'student_id',
            'name',
            'gpa',
            'dept_id',
            'major_id',
        ]
