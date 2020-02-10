from django.db import models

from profile import validators


def logo_upload_location(instance, filename):
    return 'organizations/logos/%d/%s' % (instance.pk, filename)


class Organization(models.Model):
    occupation = models.ForeignKey(to='profile.Occupation', on_delete=models.CASCADE)
    name_en = models.CharField(max_length=127)
    name_fa = models.CharField(max_length=127)
    logo = models.ImageField(null=True, upload_to=logo_upload_location)
    latitude = models.FloatField(null=True, validators=[validators.latitude])
    longitude = models.FloatField(null=True, validators=[validators.latitude])
    address_en = models.TextField(max_length=1000, null=True)
    address_fa = models.TextField(max_length=1000, null=True)
    phoneNumber = models.CharField(max_length=20, null=True)
    checked = models.BooleanField()
    creation = models.DateTimeField(auto_now_add=True)
