from django.db import models


class Stage(models.Model):
    name_en = models.CharField(max_length=60)
    name_fa = models.CharField(max_length=60)
