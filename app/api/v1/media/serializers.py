from rest_framework import serializers

from media.models import Video
from users.models import User


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner_id')

    class Meta:
        model = Video
        fields = [
            'id',
            'title',
            'original_file',
            'duration',
            'owner_id',
            'created_date'
        ]
