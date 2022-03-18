from rest_framework import permissions, viewsets

from media.models import Video
from .permissions import IsOwnerOrReadonly
from .serializers import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [
        # permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadonly
        permissions.AllowAny,
    ]
    queryset = Video.objects.all()
    #
    # def get_queryset(self):
    #     title = self.request.query_params.get('title', None)
    #     queryset = Video.objects.all()
    #
    #     if title is not None:
    #         queryset = queryset.filter(title__icontains=title.lower())
    #
    #     return queryset
