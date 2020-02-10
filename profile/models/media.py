from django.db import models


def file_upload_location(instance, filename):
    return 'media/file/%d/%s' % (instance.id, filename)


class Media(models.Model):
    FILE = 'file'
    IMAGE = 'image'
    VIDEO = 'video'
    TYPE_CHOICES = (
        (FILE, 'file'),
        (IMAGE, 'image'),
        (VIDEO, 'video'),
    )
    title = models.CharField(max_length=127)
    caption = models.TextField(max_length=1000, null=True)
    file = models.FileField(upload_to=file_upload_location)
    type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    order = models.FloatField(db_index=True)
    hidden = models.BooleanField()
    deleted = models.BooleanField()
    creation = models.DateTimeField(auto_now_add=True)
