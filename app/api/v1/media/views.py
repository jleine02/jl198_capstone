from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy

from media.models import Video
from .permissions import IsOwnerOrReadonly
from .serializers import VideoSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'videos': reverse_lazy('video-list', request=request, format=format)
    })


class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadonly
    ]
