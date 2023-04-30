from django.contrib.auth import get_user_model
from rest_framework import serializers

from App.models import Student, Department, Major
from App.serializers.department import DepartmentSerializer
from App.serializers.major import MajorSerializer


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    dept = DepartmentSerializer(read_only=True)
    major = MajorSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'student_id',
            'name',
            'gpa',
            'dept',
            'major',
        ]

    def create(self, validated_data):
        dept_id = self.initial_data.get('dept_id', None)
        major_id = self.initial_data.get('major_id', None)
        dept = Department.objects.get(pk=dept_id)
        major = Major.objects.get(pk=major_id)
        validated_data.update(dept=dept, major=major)
        return super(StudentSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        student_id = self.data.get('student_id', None)
        student = Student.objects.get(student_id=student_id)
        dept = student.dept
        major = student.major
        dept_id = self.initial_data.get('dept_id', None)
        major_id = self.initial_data.get('major_id', None)
        if dept_id is not None:
            dept = Department.objects.get(pk=dept_id)
        if major_id is not None:
            major = Major.objects.get(pk=major_id)
        validated_data.update(dept=dept, major=major)
        return super(StudentSerializer, self).update(student, validated_data)
