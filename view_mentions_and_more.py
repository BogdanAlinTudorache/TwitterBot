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
 
### VIEWING MENTIONS
mentions = api.mentions_timeline(count = 2,  tweet_mode='extended')
for mention in mentions:
    print(str(mention.id) + ' - ' + mention.full_text + " - "+ str(mention.created_at.strftime('%H:%M:%S %d-%m-%Y')), flush=True)
print()

### REPLYING TO MENTIONS
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
    
print('BNB finished running...\n', flush=True)
