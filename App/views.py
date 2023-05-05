from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from App.models import Student, User, Course, Department, Class, Teacher, Semester, CourseSelection
from App.permission import IsAdminUserOrReadOnly, IsSelfOrAdmin, IsAdminOrTeacher
from App.serializers.course_selection import CourseSelectionSerializer, StudentSelectSerializer
from App.serializers.myclass import ClassSerializer
from App.serializers.course import CourseSerializer
from App.serializers.department import DepartmentSerializer
from App.serializers.semester import SemesterSerializer
from App.serializers.student import StudentSerializer
from App.serializers.teacher import TeacherSerializer
from App.serializers.user import UserSerializer, UserRoleSerializer


# Create your views here.
class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    lookup_field = 'class_id'
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'class_id': ["exact", "icontains"],
                        'course__course_id': ["exact", "icontains"],
                        'course__name': ["exact", "icontains"],
                        'teacher__name': ["exact", "icontains"],
                        'remaining_selection': ['gte'],
                        'semester__semester_id': ['exact', 'icontains'],
                        }


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
    filterset_fields = {'student__student_id': ["exact", "icontains"],
                        'student__name': ["exact", "icontains"],
                        'class_field__course__course_id': ["exact", "icontains"],
                        'class_field__course__name': ["exact", "icontains"],
                        'class_field__teacher__name': ["exact", "icontains"],
                        'class_field__teacher__teacher_id': ["exact", "icontains"],
                        'class_field__class_id': ["exact", "icontains"],
                        'class_field__semester__semester_id': ["exact"]
                        }

    @action(methods=['post'], detail=False, permission_classes=[IsSelfOrAdmin], url_path='enroll')
    def enroll(self, request):
        serializer = StudentSelectSerializer(data=request.data)
        if request.user.username == serializer.initial_data['student_id'] or request.user.is_superuser:
            if serializer.is_valid():
                queryset = CourseSelection.objects.filter(student__student_id=request.data['student_id'],
                                                          class_field__class_id=request.data['class_id'])
                if queryset:
                    return Response({'Error': 'Already exists'}, status=status.HTTP_403_FORBIDDEN)
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Error': 'Invalid Login Credentials'}, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['post'], detail=False, permission_classes=[IsSelfOrAdmin], url_path='drop')
    def drop(self, request):
        queryset = CourseSelection.objects.get(student__student_id=request.data['student_id'],
                                               class_field__class_id=request.data['class_id'])
        serializer = StudentSelectSerializer(queryset, many=False)
        if request.user.username == serializer.data['student']['student_id'] or request.user.is_superuser:
            if serializer.data['can_drop'] == 1:
                queryset.delete()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response({'Error': 'Already have grades'}, status=status.HTTP_403_FORBIDDEN)
        return Response({'Error': 'Invalid Login Credentials'}, status=status.HTTP_403_FORBIDDEN)

    @action(methods=['get'], detail=False, permission_classes=[IsAdminUserOrReadOnly], url_path='info')
    def info(self, request):
        semester = request.data['semester_id']
        queryset = CourseSelection.objects.filter(student__student_id=request.user.username,
                                                  class_field__semester__semester_id=semester)
        serializer = CourseSelectionSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['dept_id', 'name']


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
    filterset_fields = ['student_id', 'name', 'dept__dept_id', 'dept__name']

    def perform_create(self, serializer):
        django_user = get_user_model()
        user = django_user.objects.create_user(username=serializer.validated_data['student_id'], password='password')
        serializer.save(user=user)

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()

    @action(methods=['get'], detail=False, permission_classes=[IsAdminUserOrReadOnly], url_path='info')
    def info(self, request):
        queryset = Student.objects.get(student_id=request.user.username)
        serializer = StudentSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    lookup_field = 'teacher_id'
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['teacher_id', 'name', 'dept__dept_id', 'dept__name']

    def perform_create(self, serializer):
        django_user = get_user_model()
        user = django_user.objects.create_user(username=serializer.validated_data['teacher_id'], password='password',
                                               is_staff=True)
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
            self.permission_classes = [IsAdminUserOrReadOnly]

        return super().get_permissions()

    @action(methods=['get'], detail=False, permission_classes=[IsAdminUserOrReadOnly], url_path='role')
    def role(self, request):
        queryset = User.objects.get(username=request.user.username)
        serializer = UserRoleSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)
