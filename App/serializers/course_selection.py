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
            'gpa',
            'grade',
            'can_drop',
        ]
        read_only_fields = ['grade', 'gpa']

    def create(self, validated_data):
        student_id = self.initial_data.get('student_id', None)
        class_id = self.initial_data.get('class_id', None)
        student = Student.objects.get(student_id=student_id)
        class_field = Class.objects.get(pk=class_id)
        validated_data.update(student=student, class_field=class_field, can_drop=True)
        return super(CourseSelectionSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        course_selection_id = self.data.get('course_selection_id', None)
        course_selection = CourseSelection.objects.get(pk=course_selection_id)
        student = course_selection.student
        class_field = course_selection.class_field
        student_id = self.initial_data.get('student_id', None)
        class_id = self.initial_data.get('class_id', None)
        if student_id is not None:
            student = Student.objects.get(pk=student_id)
        if class_id is not None:
            class_field = Student.objects.get(pk=class_field)
        validated_data.update(student=student, class_field=class_field)
        return super(CourseSelectionSerializer, self).update(course_selection, validated_data)


class StudentSelectSerializer(serializers.HyperlinkedModelSerializer):
    student = StudentSerializer(read_only=True)
    class_field = ClassSerializer(read_only=True)

    class Meta:
        model = CourseSelection
        fields = [
            'course_selection_id',
            'student',
            'class_field',
            'can_drop',
        ]
        read_only_fields = ['can_drop']

    def create(self, validated_data):
        student_id = self.initial_data.get('student_id', None)
        class_id = self.initial_data.get('class_id', None)
        student = Student.objects.get(student_id=student_id)
        class_field = Class.objects.get(pk=class_id)
        validated_data.update(student=student, class_field=class_field)
        return super(StudentSelectSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        course_selection_id = self.data.get('course_selection_id', None)
        course_selection = CourseSelection.objects.get(pk=course_selection_id)
        student = course_selection.student
        class_field = course_selection.class_field
        student_id = self.initial_data.get('student_id', None)
        class_id = self.initial_data.get('class_id', None)
        if student_id is not None:
            student = Student.objects.get(pk=student_id)
        if class_id is not None:
            class_field = Student.objects.get(pk=class_field)
        validated_data.update(student=student, class_field=class_field)
        return super(StudentSelectSerializer, self).update(course_selection, validated_data)
