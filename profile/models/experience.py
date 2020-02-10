from django.db import models

from profile import validators


class Experience(models.Model):
    profile = models.ForeignKey(to='profile.Profile', on_delete=models.CASCADE)
    organization = models.ForeignKey(to='profile.Organization', on_delete=models.CASCADE)
    album = models.OneToOneField(to='profile.Album', on_delete=models.CASCADE)
    title = models.CharField(max_length=127)
    about = models.TextField(max_length=1000, null=True)
    start = models.IntegerField(validators=[validators.year])
    end = models.IntegerField(null=True)
    working = models.BooleanField()
    hidden = models.BooleanField()
    deleted = models.BooleanField()
    creation = models.DateTimeField(auto_now_add=True)
