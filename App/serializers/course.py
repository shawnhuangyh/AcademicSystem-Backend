from rest_framework import serializers

from App.models import Course, Department
from App.serializers.department import DepartmentSerializer


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    dept = DepartmentSerializer(read_only=True)

    class Meta:
        model = Course
        fields = [
            'course_id',
            'name',
            'credit',
            'gp_percentage',
            'dept',
        ]

    def create(self, validated_data):
        dept_id = self.initial_data.get('dept_id', None)
        dept = Department.objects.get(pk=dept_id)
        validated_data.update(dept=dept)
        return super(CourseSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        course_id = self.data.get('course_id', None)
        course = Course.objects.get(pk=course_id)
        dept = course.dept
        dept_id = self.initial_data.get('dept_id', None)
        if dept_id is not None:
            dept = Department.objects.get(pk=dept_id)
        validated_data.update(dept=dept)
        return super(CourseSerializer, self).update(course, validated_data)
