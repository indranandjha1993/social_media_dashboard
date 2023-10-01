import tweepy
from decouple import config


class TwitterAPI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TwitterAPI, cls).__new__(cls)
            cls._instance.init_api()
        return cls._instance

    def init_api(self):
        consumer_key = config("CONSUMER_KEY")
        consumer_secret = config("CONSUMER_SECRET")
        access_token = config("ACCESS_TOKEN")
        access_token_secret = config("ACCESS_TOKEN_SECRET")

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)


def get_user(twitter_handle):
    api = TwitterAPI().api

    try:
        return api.get_user(screen_name=twitter_handle)
    except tweepy.NotFound as e:
        print(e)
        return type('', (), {})()  # Creates an empty object to mimic a user


def get_tweets(twitter_handle):
    api = TwitterAPI().api

    try:
        return api.user_timeline(screen_name=twitter_handle, count=100)
    except tweepy.Forbidden as e:
        print(e)
        return []


def get_twitter_data(twitter_handle):
    user = get_user(twitter_handle)
    tweets = get_tweets(twitter_handle)

    top_tweets = sorted(tweets, key=lambda t: t.favorite_count + t.retweet_count, reverse=True)[:10]
    hashtag_usage = {}  # Implement logic to count hashtag occurrences

    return {
        "followers_count": getattr(user, "followers_count", None),
        "following_count": getattr(user, "friends_count", None),
        "tweet_count": getattr(user, "statuses_count", None),
        "top_tweets": top_tweets,
        "hashtag_usage": hashtag_usage,
    }
