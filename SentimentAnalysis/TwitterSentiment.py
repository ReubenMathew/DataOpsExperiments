from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sentiment_mod as s

#regenerate keys if error 401
#consumer key, consumer secret, access token, access secret.
ckey="5HBjVUdE9HLMQKweJgnvY8Q7u"
csecret="YdgydiBrqteDyLNnfCV4aAyxJooYTMH2XKlyNplCIXgTuN46hr"
atoken="2851239906-hf4hyFiU8ZHngp4nBjHkdWh5kS5lA3s28aThA9i"
asecret="ScNPXTYBy22Q6ZmiPINQAMPlJOXgEAJ3i2ZvMk4PpCWP7"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]

        sentiment_value, confidence = s.sentiment(tweet)

        print(tweet,sentiment_value,confidence)

        if confidence*100 >= 80:
            output = open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()


        time.sleep(0.3)
        return True

    def on_error(self, status):
        print(status)

callback_url = "https://reubenmathew.me/"
auth = OAuthHandler(ckey, csecret,callback_url)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["trump"])