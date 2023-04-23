from rest_framework.permissions import IsAdminUser
from rest_framework import generics

from App.models import Student
from App.permission.student import IsAdminUserOrReadOnly
from App.serializers.student import StudentListSerializer, StudentDetailSerializer


# Create your views here.
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]

