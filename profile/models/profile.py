from django.db import models


def picture_upload_location(instance, filename):
    return 'profiles/pictures/%d/%s' % (instance.pk, filename)


def thumbnail_upload_location(instance, filename):
    return 'profiles/thumbnails/%d/%s' % (instance.pk, filename)


class Profile(models.Model):
    user_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to=picture_upload_location)
    thumbnail = models.ImageField(upload_to=thumbnail_upload_location)
    about = models.TextField(max_length=1000, null=True)
