from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'owner_id',
        'title',
        'original_file',
        'duration',
        'created_date'
    )
    list_display_links = ('id', 'owner_id', 'title',)


admin.site.register(Video, VideoAdmin)
