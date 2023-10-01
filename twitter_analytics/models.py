from django.db import models

from accounts.models import CustomUser


class TwitterAnalytics(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    followers_count = models.IntegerField(null=True, blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    tweet_count = models.IntegerField(null=True, blank=True)
    mentions = models.IntegerField(null=True, blank=True)
    listed_count = models.IntegerField(null=True, blank=True)
    profile_visits = models.IntegerField(null=True, blank=True)
    tweet_impressions = models.IntegerField(null=True, blank=True)
