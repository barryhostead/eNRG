import tweepy
from tweepy import OAuthHandler

import json
import csv

def GetTopNTweetsForUser(user, TopN, consumerKey, consumerSecret, accessToken, accessSecret):
    consumer_key = consumerKey
    consumer_secret = consumerSecret
    accees_token = accessToken
    access_secret = accessSecret

    auth = OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(accees_token,access_secret)

    api = tweepy.API(auth)
    tweetsToGet=TopN
    tweetArray = []
    
    try:
        tweets = api.user_timeline(screen_name=user, count=tweetsToGet )
    
        i = 0

        for status in tweets:
                jsonStatus = status._json

                #build dictionary of the required properties
                tweet = {}
                tweet["ID"] = jsonStatus["id"]
                tweet["Tweet"] = jsonStatus["text"]
                tweet["CreatedDate"] = jsonStatus["created_at"]
                tweet["User"] = jsonStatus["user"]["screen_name"]
                tweet["UserLocation"] = jsonStatus["user"]["location"]
                tweet["UserDescription"] = jsonStatus["user"]["description"]
                tweet["Source"] = jsonStatus["source"]
                tweet["HashTags"] = jsonStatus["entities"]["hashtags"]
                tweet["Mentions"] = jsonStatus["entities"]["user_mentions"]

                tweetArray.append(tweet)
    except :
        pass
    
    return tweetArray
#created_at
#text
#(entities)urls
#source
#possibly_sensitive
#user
def OutputTweets(TweetArray, outputPath):
    with open(outputPath + '%s_tweets.json' % user, 'wb') as f:           
            ##convert dictionary to JSON
            jsonTweetString = json.dumps(TweetArray).encode("utf-8")
           
            # #Output JSON to file
            f.write(jsonTweetString)
