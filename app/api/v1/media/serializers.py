from rest_framework import serializers

from media.models import Video
from users.models import User


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    owner_id = serializers.ReadOnlyField(source='owner_id.id')

    class Meta:
        model = Video
        fields = [
            'owner_id',
            'id',
            'title',
            'original_file',
            'duration',
            'created_date'
        ]
