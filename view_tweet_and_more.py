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

tweet = api.get_status(id = 1473313037411094545, trim_user = False, include_ext_alt_text=False, include_card_uri=False )

print('### Printing tweet:\n')
print("Text:", tweet.text)
print("Source:", tweet.source)
print('User name:', tweet.user.name)
print("User screen name:", tweet.user.screen_name)
print("User followers:", tweet.user.followers_count)

print()



print('BNB finished running...\n', flush=True)
