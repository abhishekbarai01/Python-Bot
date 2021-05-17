import tweepy
import time


consumer_key = "1YMSkyR893TmjboMMwzDXGlby"
consumer_secret = 'EyROjPG1sY5iWRs1ez4CngobtAXt0ebRXwBRM53fph8baRvIZk'

key = '1393610684567457792-jgtRpuCYNATIijx0uclyyP3YwiYAkW'
secret = 'XrWP6EmnbiwL4K74E6RplpZDwukTP19RC6i0uV0dE2WB9'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
hashtag = "100daysofcode" or "#python"
tweetNumber = 10
tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)

def searchbot():
    for tweet in tweets:
        try:
            tweet.retweet()
            api.create_favorite(tweet.id)
            print("Retweet Done!")
            time.sleep(2)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(2)

searchbot()