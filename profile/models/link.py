from django.db import models


class Link(models.Model):
    link = models.URLField()
    anchor = models.CharField(max_length=127, null=True)
