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
 
tweet = 'Hello from the dark side! This is the BerryNews Bot\nCall me, BNB.'
if len(tweet) <160:
    print('Posting tweet:', tweet,'\n')
    api.update_status(tweet)
else:
    print('Tweet is bigger than 150 characers, stopping...')
    print(len(tweet))
    sys.exit()
    
print('BNB finished running...\n', flush=True)
