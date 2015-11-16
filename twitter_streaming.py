#Import tweepy libraries
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Assign your Twitter Application's credentials to Variables
consumer_key = "ENTER YOUR CONSUMER KEY (API KEY) FROM TWITTER.COM"
consumer_secret = "ENTER YOUR CONSUMER SECRET (API SECRET) FROM TWITTER.COM"
access_token = "ENTER YOUR ACCESS TOKEN FROM TWITTER.COM
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET FROM TWITTER.COM"


class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #Connect to and authenticate with Twitter API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    
    stream.filter(track=['deflategate'])