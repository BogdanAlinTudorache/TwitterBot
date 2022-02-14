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
 
## GET USER BY NAME
user = api.get_user(screen_name="berrynewsorg")
print("User details:")
print('id:',user.id)
print('name:',user.name)
print('description',user.description)
print('location:',user.location)
print()
