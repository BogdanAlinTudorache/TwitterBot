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
 


## UPLOADING PHOTO
media = api.media_upload('/home/ubuntu/Desktop/Projects/BerryNews/TwitterBot/chrome_berry_news_dino.jpg')
print(media)
media_ids = media.media_id
print("ACTION: Upload successful!: ",media_ids)

# media_ids=1494378579026759685

### POSTING MEDIA
tweet_media = "You know where to find us!\nMuch ❤️‍🔥,\nBNB🍓"
if len(tweet_media) <160:
    print('Posting tweet:', tweet_media,'\n')
    try:
        api.update_status(tweet_media, media_ids = [media_ids])
        print('ACTION: Replied to tweeet\n')
    except e as Exception: 
        print(Exception)
else:
    print('Tweet is bigger than 150 characers, stopping...')
    print(len(tweet_media))
    


print('BNB finished running...\n', flush=True)
