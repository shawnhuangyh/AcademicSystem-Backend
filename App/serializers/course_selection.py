from rest_framework import serializers

from App.models import CourseSelection, Student, Class
from App.serializers.myclass import ClassSerializer
from App.serializers.student import StudentSerializer


class CourseSelectionSerializer(serializers.HyperlinkedModelSerializer):
    student = StudentSerializer(read_only=True)
    class_field = ClassSerializer(read_only=True)

    class Meta:
        model = CourseSelection
        fields = [
            'course_selection_id',
            'student',
            'class_field',
            'gp',
            'exam',
            'grade',
        ]
        read_only_fields = ['grade']

    def create(self, validated_data):
        student_id = self.initial_data.get('student_id', None)
        class_id = self.initial_data.get('class_id', None)
        student = Student.objects.get(student_id=student_id)
        class_field = Class.objects.get(pk=class_id)
        validated_data.update(student=student, class_field=class_field)
        return super(CourseSelectionSerializer, self).create(validated_data)
