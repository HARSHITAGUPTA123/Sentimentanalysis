from __future__ import print_function
#from pprint import pprint
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentimentanalysis as s
from mytwitterkeys import *



class listener(StreamListener):
    
    
    def on_data(self, data):
       #if you directly print data,it will show all of the data with whole json for a tweet.But since we only want the twitter text and no other info,we will extract it only
     
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

#imported my keys and secrets through module
auth = OAuthHandler(ckey(), csecret())
auth.set_access_token(atoken(), asecret())

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
