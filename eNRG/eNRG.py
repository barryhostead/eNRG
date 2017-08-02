from ScrapeWebsite import *
from GetTweets import *
from TweetParser import *
from JSONHelper import *
from GeoLocationData import *

map_1

###Parse Twitter Data
##Get the number of tweets to retrieve.
#TopN = 10000
#consumerKey = 'ipTb7DZ0LbJ18p9ATjdrSQ23p'
#consumerSecret = 'DT9OroScZI4HoGbx7PkRL6ojir5T4GWvmlqCkPTd9MgH72fHE9'
#acceesToken = '421348331-vDfvREGRolF3dA4mvvMrihZRtTohQ4yQmoXhRQjX'
#accessSecret = 'w8zsnlGfm6G54wmlKS1Glz9sk0Ei595y6zmPuikQKn5da'

#filepath = "C:\\Users\\barry\\Documents\\GitHub\\eNRG\\eNRG\\"
#fileEnding = "_tweets.json"

#thinkgeoenergy = 'thinkgeoenergy'
#GeothermEneRRgy = 'GeothermEneRRgy'
#GRC2001 = 'GRC2001'

#thinkgeoenergy_file = filepath + thinkgeoenergy + fileEnding
#GeothermEneRRgy_file =  filepath + 'GeothermEneRRgy' + fileEnding
#GRC2001_file =  filepath + 'GRC2001' + fileEnding

#TweetArray = []

##Get Tweets for user = "thinkgeoenergy"
#TweetArray.extend(GetTopNTweetsForUser(thinkgeoenergy, TopN, consumerKey, consumerSecret, acceesToken, accessSecret))

###Get Tweets for user = "GeothermEneRRgy"
#TweetArray.extend(GetTopNTweetsForUser(GeothermEneRRgy, TopN, consumerKey, consumerSecret, acceesToken, accessSecret))

###Get Tweets for user = "GRC2001"
#TweetArray.extend(GetTopNTweetsForUser(GRC2001, TopN, consumerKey, consumerSecret, acceesToken, accessSecret))
                                                                                                                                                                                                                                     
##parse the tweet array
##pull out all of the hash tags
#HashTags = []
#HashTags = ParseHashTags(TweetArray)

##Mentions
#Mentions = []
#Mentions = ParseMentions(TweetArray)
