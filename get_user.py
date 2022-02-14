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
 
## POSTING TWEET
nl_en_link = "http://berrynews.org/netherlands-en.html"
ro_en_link = "http://berrynews.org/romania-en.html"
ro_ro_link = "http://berrynews.org/romania-ro.html"
text="Gazele s-au scumpit din cauza rușilor,spune ministrul Energiei"
tweet = "BNB:\n"+text+"\n"+ ro_ro_link +"\n#twitterbot #stiri #romania #berrynews"  

tweet = '@b_tudorache#Hello from the dark side!'
# if len(tweet) <160:
#     print('Posting tweet:', tweet,'\n')
#     api.update_status(tweet, in_reply_to_status_id=  1469339850851729412)
# else:
#     print('Tweet is bigger than 150 characers, stopping...')
#     print(len(tweet))
#     sys.exit()

## NOT WORKING
user = api.get_user(screen_name="berrynewsorg")
print("User details:")
print('id:',user.id)
print('name:',user.name)
print('description',user.description)
print('location:',user.location)
print()
