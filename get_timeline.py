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
 

## PRINTING OWN TIMELINE
print('### Printing own timeline:\n')
timeline = api.home_timeline(count=1)


for tweet in timeline:
   
    time = tweet.created_at.strftime('%H:%M:%S %d-%m-%Y')
    print(f"AT: {time}\nUSER ID: {tweet.user.id}\nUSER: {tweet.user.name}\nSAID: {tweet.text} \n")
    print("############################################################\n")
  
print()

# PRINTING USER TIMELINE
print('### Printing user timeline:\n')
timeline = api.user_timeline(screen_name="b_tudorache", count=2)
for tweet in timeline:
     
     print(f"USER {tweet.user.name} \nSAID {tweet.text} \nAT {tweet.created_at}\n")
     print("############################################################\n")

