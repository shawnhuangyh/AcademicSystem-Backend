from rest_framework import generics, viewsets

from App.models import Student
from App.permission import IsAdminUserOrReadOnly
from App.serializers.student import StudentSerializer


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'student_id'
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()
