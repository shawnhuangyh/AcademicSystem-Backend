from rest_framework import serializers

from App.models import Semester


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = [
            'semester_id',
            'name',
        ]
