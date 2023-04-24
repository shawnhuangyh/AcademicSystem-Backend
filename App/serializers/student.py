from django.contrib.auth import get_user_model
from rest_framework import serializers

from App.models import Student, Department, Major
from App.serializers.department import DepartmentListSerializer
from App.serializers.major import MajorListSerializer


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    dept = DepartmentListSerializer(read_only=True)
    major = MajorListSerializer(read_only=True)

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
        django_user = get_user_model()
        user = django_user.objects.create_user(username=self.initial_data.get('student_id', None), password='password')
        dept_id = self.initial_data.get('dept_id', None)
        major_id = self.initial_data.get('major_id', None)
        dept = Department.objects.get(pk=dept_id)
        major = Major.objects.get(pk=major_id)
        validated_data.update(user=user, dept=dept, major=major)
        return super(StudentSerializer, self).create(validated_data)
