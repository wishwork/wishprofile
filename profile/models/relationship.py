from django.db import models


class Relationship(models.Model):
    title_en = models.CharField(max_length=127)
    title_fa = models.CharField(max_length=127)
