# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:37:56 2018

@author: Yusra
"""

import tweepy
from tweepy import OAuthHandler
from IPython.display import display
from tweepy import Stream
from tweepy.streaming import StreamListener
import emoji

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def  twitter_Access():
     auth = OAuthHandler(consumer_key, consumer_secret)
     auth.set_access_token(access_token, access_secret)
     api = tweepy.API(auth, wait_on_rate_limit=True)
     return api

extract = twitter_Access()

# Knowing your rate limits, or data calls available for Twitter API
data = extract.rate_limit_status()
display(data)
print (data['resources']['statuses']['/statuses/home_timeline'])
print (data['resources']['users']['/users/lookup'])


# Updating your status
extract.update_status(status='UpdatingfromPython')

#The first 10 tweets on your timeline;
for tweets in tweepy.Cursor(extract.home_timeline).items(5):
    print(tweets.text)

#You can also retrive tweets in json format
for tweets in tweepy.Cursor(extract.home_timeline).items(5):
    print(tweets._json)

# To retrive the list of all your followers (only json format works here)
for friend in tweepy.Cursor(extract.friends).items():
    print(friend)

#To get a list of your own tweets
for tweet in tweepy.Cursor(extract.user_timeline).items():
    print(tweet.text)

#Searching tweets with a specified query
Royalwed = extract.search(q="Royal Wedding", tweet_mode="extended")
for tweet in Royalwed[:5]:
    print(tweet.full_text)
    print()
    
#Streaming tweets
class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
twitter_stream = Stream(auth, listener())
twitter_stream.filter(track='car')

#searching tweets with specific emojis
ThumbsUp = emoji.emojize(':thumbs_up:')
print(ThumbsUp)

emoji = extract.search(q=ThumbsUp, count=5, tweet_mode='extended')
for tweet in emoji:
    print(tweet.full_text)


    
