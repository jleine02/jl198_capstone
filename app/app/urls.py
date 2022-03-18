from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),  # just until frontend is added
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('rest_framework.urls')),
]
