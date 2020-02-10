from django.db import models


def icon_upload_location(instance, filename):
    return 'occupation/icons/%d/%s' % (instance.pk, filename)


class Occupation(models.Model):
    icon = models.ImageField(upload_to=icon_upload_location)
    name_en = models.CharField(max_length=50)
    name_fa = models.CharField(max_length=50)
