import tweepy
from tweepy import OAuthHandler

CONSUMER_KEY = 'lPNchIfwCLd0AnJbLG6IfHyvY'
CONSUMER_SECRET = 'ICm639pX5uWmvtYrYR9NysrrZAQQCdZbl9VFjVXXAXl9SkIp30'
OAUTH_TOKEN = '20432318-seggLOx73igoOf37kNCYr40ViTI91fokO8rwG041m'
OAUTH_TOKEN_SECRET = 'YKDzwih61fusSgwt15K79rxHbELNUZjNoapKJwlkqfULf'

def get_auth():
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    return auth

def get_api():
    auth = get_auth()
    return tweepy.API(auth)

# api = tweepy.API(auth)