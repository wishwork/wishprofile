from django.db import models

from profile import validators


class Recommendation(models.Model):
    relationship = models.ForeignKey(to='profile.Relationship', null=True, on_delete=models.SET_NULL)
    comment = models.TextField(max_length=2000, validators=[validators.min_length(30)])
    link = models.ForeignKey(to='profile.Link', null=True, on_delete=models.SET_NULL)
    profile = models.ForeignKey(to='profile.Profile',
                                on_delete=models.CASCADE,
                                related_name='recommendations',
                                related_query_name='recommendation')
    publisher = models.ForeignKey(to='profile.Profile',
                                  on_delete=models.CASCADE,
                                  related_name='published_recommendations',
                                  related_query_name='published_recommendations')
    hidden = models.BooleanField()
    deleted = models.BooleanField()
    creation = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
