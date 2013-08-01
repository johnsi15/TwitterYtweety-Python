# -*- coding: utf-8 -*-
import tweepy

consumer_key="j384OSKRvppRTV31MWCjSQ"
consumer_secret="YkeMBytnY7ohwXG86gU2X91UG5eLYdhfDaYyPTQzsM"

access_token="239525380-9QOxpQ4xsgUwAZyQYH7yotU2YORD7JRIKFityqmo"
access_token_secret="WD6SLS2MWKj6pcACEPcdXeBZSA0PZD5EuShuz4s1mks"

auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
#status=api.user_timeline(id="mejorandola")
status = api.search(q="mejorandola")
for status in status:
    if status:
        #print status.__getstate__()
        print status.text