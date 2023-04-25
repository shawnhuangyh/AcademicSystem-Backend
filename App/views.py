from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action

from App.models import Student, User, Course, Department, Class, Teacher, Major, Semester, CourseSelection
from App.permission import IsAdminUserOrReadOnly, IsSelfOrAdmin, IsAdminOrTeacher
from App.serializers.course_selection import CourseSelectionSerializer
from App.serializers.myclass import ClassSerializer
from App.serializers.course import CourseSerializer
from App.serializers.department import DepartmentSerializer
from App.serializers.major import MajorSerializer
from App.serializers.semester import SemesterSerializer
from App.serializers.student import StudentSerializer
from App.serializers.teacher import TeacherSerializer
from App.serializers.user import UserSerializer


# Create your views here.
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'class_id'
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['class_id', 'course__course_id', 'course__name', 'class_no', 'teacher__name']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'course_id'
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course_id', 'name', 'dept__name']


class CourseSelectionViewSet(viewsets.ModelViewSet):
    queryset = CourseSelection.objects.all()
    serializer_class = CourseSelectionSerializer
    lookup_field = 'course_selection_id'
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student__student_id', 'student__name', 'class_field__course__course_id',
                        'class_field__course__name', 'class_field__class_no', 'class_field__teacher__name',
                        'class_field__teacher__teacher_id', 'class_field__class_id']


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dept_id', 'name']


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.all()
    serializer_class = MajorSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['major_id', 'name']


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['semester_id', 'name']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['student_id', 'name', 'dept__dept_id', 'dept__name', 'major__major_id', 'major__name']

    def perform_create(self, serializer):
        django_user = get_user_model()
        user = django_user.objects.create_user(username=serializer.validated_data['student_id'], password='password')
        serializer.save(user=user)

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'teacher_id'
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher_id', 'name', 'dept__dept_id', 'dept__name']


    def perform_create(self, serializer):
        django_user = get_user_model()
        user = django_user.objects.create_user(username=serializer.validated_data['teacher_id'], password='password')
        serializer.save(user=user)

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'PUT':
            self.permission_classes = [IsSelfOrAdmin]
        else:
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()
