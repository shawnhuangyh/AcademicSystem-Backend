from django.contrib.auth import get_user_model
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser
from rest_framework.response import Response

from App.models import Student, User
from App.permission import IsAdminUserOrReadOnly, IsSelfOrReadOnly, IsAdminOrTeacher
from App.serializers.student import StudentSerializer
from App.serializers.user import UserSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'
    permission_classes = [IsAdminOrTeacher]

    def perform_create(self, serializer):
        django_user = get_user_model()
        user = django_user.objects.create_user(username=serializer.validated_data['student_id'], password='password')
        serializer.save(user=user)

    def perform_destroy(self, instance):
        instance.user.delete()
        instance.delete()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticatedOrReadOnly, IsSelfOrReadOnly]
        else:
            self.permission_classes = [IsAdminUser]

        return super().get_permissions()
