# pip install tweepy if you don't have tweepy installed
import tweepy
import pandas as pd
import time

#user credentials to authenticate API
#you will get these credentilas when creating a developer account on Twitter
consumer_key = "vTThgHQHpYvkpEfdYuyBSGCLr"
consumer_secret = "XhcSbhm7Jr5d3xa5YB2JHAq70qJMo1Y4nz7XNFJWuyurH1w9tC"
access_token = "1036956127949475840-vubjDPN5YEDxKaZ0kSDDN1k9i9pQGb"
access_token_secret = "3WtSEojsuSzLiGpfqAhYy6oMoJb0fnOs89ZdZhdi7OAPS"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

#creating a list of tweets
tweets = []

#specify whose tweets you're scraping
username = 'Trump'
#number of tweets you need
tweets_num = 100

#defining a converting function which takes username and count as parameters
def tweets_to_csv(username,tweets_num):

        #getting the individual tweets
        for tweet in api.user_timeline(user_id=username, count=tweets_num):

            #adding tweets to the list
            tweets.append((tweet.created_at,tweet.id,tweet.text))

            #creating a dataframe in pandas and defining column names
            df = pd.DataFrame(tweets,columns=['Date', 'Tweet_ID', 'Message'])

            #converting dataframe to CSV file
            df.to_csv('formatted_tweets.csv')


#calling the function to create the CSV file
tweets_to_csv(username, tweets_num)