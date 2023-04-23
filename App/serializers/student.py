from rest_framework import serializers

from App.models import Student, Department, Major


class StudentListSerializer(serializers.ModelSerializer):
    dept_id = serializers.IntegerField(source='dept.dept_id')
    major_id = serializers.IntegerField(source='major.major_id')

    class Meta:
        model = Student
        fields = [
            'student_id',
            'name',
            'gpa',
            'dept_id',
            'major_id',
        ]

    def create(self, validated_data):
        dept_id = self.initial_data.get('dept_id', None)
        major_id = self.initial_data.get('major_id', None)
        dept = Department.objects.get(pk=dept_id)
        major = Major.objects.get(pk=major_id)
        validated_data.update(dept=dept, major=major)
        return super(StudentListSerializer, self).create(validated_data)


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
