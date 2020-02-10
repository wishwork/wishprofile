from django.db import models

from profile import validators


class Education(models.Model):
    profile = models.ForeignKey(to='profile.Profile', on_delete=models.CASCADE)
    organization = models.ForeignKey(to='profile.Organization', on_delete=models.CASCADE)
    major = models.ForeignKey(to='profile.Major', on_delete=models.CASCADE)
    stage = models.ForeignKey(to='profile.Stage', on_delete=models.CASCADE)
    album = models.OneToOneField(to='profile.Album', on_delete=models.CASCADE)
    link = models.ForeignKey(to='profile.Link', null=True, on_delete=models.SET_NULL)
    about = models.TextField(max_length=1000, null=True)
    start = models.IntegerField(validators=[validators.year])
    end = models.IntegerField(null=True, validators=[validators.year])
    grade = models.FloatField(validators=[validators.grade])
    hidden = models.BooleanField()
    deleted = models.BooleanField()
    creation = models.DateTimeField(auto_now_add=True)
