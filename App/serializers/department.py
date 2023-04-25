from rest_framework import serializers

from App.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            'dept_id',
            'name',
            'address',
            'phone',
        ]
