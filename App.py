import tweepy
import time
    
class Tweeper:
    def __init__(self, API_key, API_secret, token, token_secret):
        auth = tweepy.OAuthHandler(API_key, API_secret)
        auth.set_access_token(token, token_secret)
        
        self.api = tweepy.API(auth)

    def sendTweet(self, message):
        self.api.update_status(message)
        

