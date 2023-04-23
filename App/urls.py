from django.urls import path, include

from App.views import StudentList, StudentDetail

app_name = 'v1'

urlpatterns = [
    path('student/', StudentList.as_view(), name='student_list'),
    path('student/<int:pk>', StudentDetail.as_view(), name='student_detail'),
]
