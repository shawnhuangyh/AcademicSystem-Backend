from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from App.models import Student
from App.serializers import StudentListSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentListSerializer(student, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
