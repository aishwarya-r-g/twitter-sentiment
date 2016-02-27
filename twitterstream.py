import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import argparse
import string
import json

api_key = "OCXWtMXtYXmCmKb5J1Lk8VJFK"
api_secret = "dH3HLT8gwU3f2ntZAAZJCKKdLaBFqi3k9mx304IxigFyxZGUwm"
access_token_key = "332676261-bp0bshHiyEaO7CvKvwAUC3gSQ6Omr5u1W2OkwQ8E"
access_token_secret = "jXp2S2MYYveMArZdis8YbXJamIDO0gRxBVIm7vScu7Qfw"


class MyListener(StreamListener):
    """Custom StreamListener for streaming data."""

    
    def on_data(self, data):
        print data
        return True
        #time.sleep(5)
        return True
    
    def on_error(self, status):
        print(status)
        return True




if __name__ == '__main__':

    auth = OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    api = tweepy.API(auth)
    #print "hello"
    
    twitter_stream = tweepy.Stream(auth, MyListener())
    twitter_stream.filter(track= ['jnu', 'JNU', 'Jnu'])