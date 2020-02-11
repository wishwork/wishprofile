from django.db import models

from profile import validators


class Accomplishment(models.Model):
    PROJECT = 'project'
    PUBLICATION = 'publication'
    CERTIFICATE = 'certificate'
    TYPE_CHOICES = (
        (PROJECT, 'Project'),
        (PUBLICATION, 'Publication'),
        (CERTIFICATE, 'Certificate'),
    )
    profile = models.ForeignKey(to='profile.Profile', on_delete=models.CASCADE)
    organization = models.ForeignKey(to='profile.Organization', null=True, on_delete=models.SET_NULL)
    link = models.ForeignKey(to='profile.Link', null=True, on_delete=models.SET_NULL)
    album = models.OneToOneField(to='profile.Album', on_delete=models.CASCADE)
    type = models.CharField(max_length=11, choices=TYPE_CHOICES)
    title = models.CharField(max_length=127)
    about = models.TextField(max_length=1000, null=True)
    year = models.IntegerField(null=True, validators=[validators.year])
    order = models.FloatField()
    hidden = models.BooleanField()
    deleted = models.BooleanField()
    creation = models.DateTimeField(auto_now_add=True)
