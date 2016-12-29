from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentimentanalysis as s
from mytwitterkeys import *

class listener(StreamListener):

    def on_data(self, data):
       #if you directly print data,it will show all of the data with whole json for a tweet.But since we only want the twitter text and no other info,we will extract it only
        all_data = json.loads(data)
        tweet = all_data['text']
        
        sent,conf = s.sentiment(tweet)
        
        print tweet,sent,conf
        
        if conf*100 >=80:#if it a tweet with very good confidence value,we will write it in a file
            output = open('twitter.txt','a')
            output.write(sent)
            output.write('\n')
            output.close()
        
        
        return(True)

    def on_error(self, status):
        print status

#imported my keys and secrets through module
auth = OAuthHandler(ckey(), csecret())
auth.set_access_token(atoken(), asecret())

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["narendra modi"])
