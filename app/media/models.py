from uuid import uuid4
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Video(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, blank=False)
    original_file = models.FileField(
        blank=False,
        upload_to="dest path",
        validators=[FileExtensionValidator(['mp4', 'mov', 'mpeg'])]
    )
    original_size = models.IntegerField(
        _('video size in kilobytes'),
        blank=True,
        null=True
    )
    duration = models.IntegerField(
        _('duration'),
        blank=True,
        null=True
    )
    owner_id = models.ForeignKey(
        'users.User',
        related_name='videos',
        null=True,
        on_delete=models.SET_NULL
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_date', 'duration')

    def __str__(self):
        return self.title
