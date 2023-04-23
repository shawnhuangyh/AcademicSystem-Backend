from django.urls import path, include

from App.views import student_list

app_name = 'v1'

urlpatterns = [
    path('student/', student_list, name='student'),
]
