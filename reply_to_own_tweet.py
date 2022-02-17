import tweepy
import time
import sys

# NOTE: I put my keys in the credentials.py to separate them
# from this main file.
# Please refer to credentials.py to see the format.
from credentials import twitter_bot_keys

# NOTE: flush=True is just for running this script
print('\nThis is my twitter bot: BerryNews Bot - BNB.\nStarted running...', flush=True)

auth = tweepy.OAuthHandler(twitter_bot_keys['API Key'], twitter_bot_keys['API Key Secret'])
auth.set_access_token(twitter_bot_keys['Access Token'], twitter_bot_keys['Access Token Secret'])
api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK\n")
except:
    print("Error during authentication\n")
 
timeline = api.user_timeline(screen_name="berrynewsorg", count=2,exclude_replies=False)
print("Last tweet id:",timeline[0].id)
last_tweet_id = timeline[0].id

reply_of_tweet = "Still here.\nWith <3 BNB🍓."

if len(reply_of_tweet) <160:
    print('Posting tweet:', reply_of_tweet,'\n')
    api.update_status(reply_of_tweet, in_reply_to_status_id=last_tweet_id)
else:
    print('Tweet is bigger than 150 characers, stopping...')
    print(len(tweet))
    sys.exit()
