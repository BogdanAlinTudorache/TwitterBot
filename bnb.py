import tweepy
import time
import sys

# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from credentials import twitter_bot_keys

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
print('\nThis is my twitter bot: BerryNews Bot - BNB.\nStarted running...', flush=True)

auth = tweepy.OAuthHandler(twitter_bot_keys['API Key'], twitter_bot_keys['API Key Secret'])
auth.set_access_token(twitter_bot_keys['Access Token'], twitter_bot_keys['Access Token Secret'])
api = tweepy.API(auth)


try:
    api.verify_credentials()
    print("Authentication OK\n")
except:
    print("Error during authentication\n")


## VIEW TWEET
tweet = api.get_status(id = 1473313037411094545, trim_user = False, include_ext_alt_text=False, include_card_uri=False )

print('### Printing tweet:\n')
print("Text:", tweet.text)
print("Source:", tweet.source)
print('User name:', tweet.user.name)
print("User screen name:", tweet.user.screen_name)
print("User followers:", tweet.user.followers_count)
print()


### POSTING TWEET
tweet = 'Hello from the dark side! This is the BerryNews Bot\nCall me, BNB.'
if len(tweet) <160:
    print('Posting tweet:', tweet,'\n')
    api.update_status(tweet)
else:
    print('Tweet is bigger than 150 characters, stopping...')
    print(len(tweet))
    sys.exit()


### REPLYING TO OWN TWEET

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

# ## GET USER DETAILS
user = api.get_user(screen_name="criptoBilbo")
print("User details:")
print('id:',user.id)
print('name:',user.name)
print('description',user.description)
print('location:',user.location)
# print()

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
timeline = api.user_timeline(screen_name="berrynewsorg", count=2)
for tweet in timeline:

     print(f"USER {tweet.user.name} \nSAID {tweet.text} \nAT {tweet.created_at}\n")
     print(tweet.id)
     print("############################################################\n")



# Profile banner
print("User details:",
      api.get_settings()['screen_name'])


### VIEWWING MENTIONS AND REPLYING TO THEM
mentions = api.mentions_timeline(count = 2,  tweet_mode='extended')
for mention in mentions:
    print(str(mention.id) + ' - ' + mention.full_text + " - "+ str(mention.created_at.strftime('%H:%M:%S %d-%m-%Y')), flush=True)
print()
last_mention_id = mentions[0].id
print("Last mention id:", last_mention_id)
reply_of_mention= ' Yes, but there is only one BNB🍓.\nCheers🍻'
username_reply = mentions[0].user.screen_name 
print(username_reply)

tweet_reply = str( '@' + username_reply + reply_of_mention)
if len(tweet_reply) <160:
    print('Posting tweet:', tweet_reply,'\n')
    try: 
        api.update_status(tweet_reply, in_reply_to_status_id = last_mention_id)
        print('ACTION: Replied to tweeet\n')
    except e:
        print(e)
else:
    print('Tweet is bigger than 150 characers, stopping...')
    print(len(tweet_reply))
   
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
