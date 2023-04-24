from rest_framework import serializers

from App.models import Major


class MajorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        fields = [
            'major_id',
            'name',
        ]
