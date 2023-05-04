from django.contrib.auth import get_user_model
from rest_framework import serializers

from App.models import Student, Department
from App.serializers.department import DepartmentSerializer


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    dept = DepartmentSerializer(read_only=True)

    class Meta:
        model = Student
        fields = [
            'student_id',
            'name',
            'gpa',
            'dept',
        ]

    def create(self, validated_data):
        dept_id = self.initial_data.get('dept_id', None)
        dept = Department.objects.get(pk=dept_id)
        validated_data.update(dept=dept)
        return super(StudentSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        student_id = self.data.get('student_id', None)
        student = Student.objects.get(student_id=student_id)
        dept = student.dept
        dept_id = self.initial_data.get('dept_id', None)
        if dept_id is not None:
            dept = Department.objects.get(pk=dept_id)
        validated_data.update(dept=dept)
        return super(StudentSerializer, self).update(student, validated_data)
