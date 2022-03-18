from django.urls import path, include

from .views import api_root, VideoViewSet


urlpatterns = [
    path('', api_root, name='api-root'),
    path('videos/', VideoViewSet, name='video-list'),
]
