#!/usr/bin/env python
from keys import *
import tweepy
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

API = tweepy.API(auth)
Tweet = raw_input('Tweet: ')
API.update_status(Tweet)