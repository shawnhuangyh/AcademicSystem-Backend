from rest_framework import serializers

from App.models import Class


class MajorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = [
            'major_id',
            'name',
        ]
