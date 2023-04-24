from rest_framework import serializers

from App.models import Major


class MajorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Major
        fields = [
            'major_id',
            'name',
        ]
