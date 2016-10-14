import json
import tweepy
from tweepy import OAuthHandler
from collections import Counter
from prettytable import PrettyTable

CONSUMER_KEY = 'lPNchIfwCLd0AnJbLG6IfHyvY'
CONSUMER_SECRET = 'ICm639pX5uWmvtYrYR9NysrrZAQQCdZbl9VFjVXXAXl9SkIp30'
OAUTH_TOKEN = '20432318-seggLOx73igoOf37kNCYr40ViTI91fokO8rwG041m'
OAUTH_TOKEN_SECRET = 'YKDzwih61fusSgwt15K79rxHbELNUZjNoapKJwlkqfULf'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

count = 50
query = 'Weather'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]
hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]
words = [w for t in status_texts
         for w in t.split()]

for entry in [screen_names, hashtags, words]:
    counter = Counter(entry)
    print counter.most_common()[:10]  # the top 10 results
    print

for label, data in (('Text', status_texts),('Screen Name', screen_names),('Word', words)):
     table = PrettyTable(field_names=[label, 'Count'])
     counter = Counter(data)
     [ table.add_row(entry) for entry in counter.most_common()[:10] ]
     table.align[label], table.align['Count'] = 'l', 'r' # align the columns
     print table