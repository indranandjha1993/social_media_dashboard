from django.shortcuts import render, redirect

from .models import TwitterAnalytics
from .utils import get_twitter_data


def user_analytics(request):
    if request.user.is_authenticated:
        twitter_data = get_twitter_data(request.user.twitter_handle)

        analytics, created = TwitterAnalytics.objects.get_or_create(user=request.user)

        analytics.followers_count = twitter_data.get("followers_count")
        analytics.following_count = twitter_data.get("following_count")
        analytics.tweet_count = twitter_data.get("tweet_count")

        analytics.save()

        context = {
            "analytics": analytics,
        }
        return render(request, "analytics/user-analytics.html", context)

    else:
        return redirect("login")
