from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

CONSUMER_KEY = 'lPNchIfwCLd0AnJbLG6IfHyvY'
CONSUMER_SECRET = 'ICm639pX5uWmvtYrYR9NysrrZAQQCdZbl9VFjVXXAXl9SkIp30'
OAUTH_TOKEN = '20432318-seggLOx73igoOf37kNCYr40ViTI91fokO8rwG041m'
OAUTH_TOKEN_SECRET = 'YKDzwih61fusSgwt15K79rxHbELNUZjNoapKJwlkqfULf'

keyword_list = ['starwars', 'rogue one']  # track list
limit = 100


class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print("Failed on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)