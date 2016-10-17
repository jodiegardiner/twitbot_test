from twit_api import api
import tweepy

for status in tweepy.Cursor(api.user_timeline, id="richardadalton").items(10):
    # Process a tweet
    print(status.text)