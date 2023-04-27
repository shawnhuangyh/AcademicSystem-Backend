from rest_framework import serializers

from App.models import Class, Course, Semester, Teacher
from App.serializers.course import CourseSerializer
from App.serializers.semester import SemesterSerializer
from App.serializers.teacher import TeacherSerializer


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    course = CourseSerializer(read_only=True)
    semester = SemesterSerializer(read_only=True)
    teacher = TeacherSerializer(read_only=True)

    class Meta:
        model = Class
        fields = [
            'class_id',
            'course',
            'semester',
            'teacher',
            'classroom',
            'time',
            'start',
            'end',
            'current_selection',
            'max_selection',
            'remaining_selection'
        ]
        read_only_fields = ['current_selection', 'remaining_selection']

    def create(self, validated_data):
        course_id = self.initial_data.get('course_id', None)
        semester_id = self.initial_data.get('semester_id', None)
        teacher_id = self.initial_data.get('teacher_id', None)
        course = Course.objects.get(pk=course_id)
        semester = Semester.objects.get(pk=semester_id)
        teacher = Teacher.objects.get(teacher_id=teacher_id)
        validated_data.update(course=course, semester=semester, teacher=teacher)
        return super(ClassSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        class_id = self.data.get('class_id', None)
        class_instance = Class.objects.get(pk=class_id)
        course = class_instance.course
        semester = class_instance.semester
        teacher = class_instance.teacher
        course_id = self.initial_data.get('course_id', None)
        semester_id = self.initial_data.get('semester_id', None)
        teacher_id = self.initial_data.get('teacher_id', None)
        if course_id is not None:
            course = Course.objects.get(pk=course_id)
        if semester_id is not None:
            semester = Semester.objects.get(pk=semester_id)
        if teacher_id is not None:
            teacher = Teacher.objects.get(teacher_id=teacher_id)
        validated_data.update(course=course, semester=semester, teacher=teacher)
        return super(ClassSerializer, self).update(class_instance, validated_data)
