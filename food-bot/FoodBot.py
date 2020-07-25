import praw
import tweepy
import time

# Timer constant - 12H
INTERVAL = 60 * 60 * 12

# Fill in keys
Reddit_ClientID =
Reddit_SecretID =
Reddit_Agent =

Twitter_APIKey =
Twitter_APISecret =
Twitter_AccessToken =
Twitter_AccessSecret =

# Bot that takes top daily submissions from r/food and tweets them every 12H
def FoodBot():
    # Authenticate to reddit
    reddit = praw.Reddit(client_id = Reddit_ClientID,
                         client_secret = Reddit_SecretID,
                         user_agent = Reddit_Agent)

    # Authenticate to twitter
    auth = tweepy.OAuthHandler(Twitter_APIKey,
                               Twitter_APISecret)

    auth.set_access_token(Twitter_AccessToken,
                          Twitter_AccessSecret)

    twitter = tweepy.API(auth)

    while True:
        # List generator of r/food filtered by top daily
        top_submissions = reddit.subreddit('food').top(time_filter='day', limit=2)
        
        # Go through top submissions tweeting 1 every 12H
        try:
            for submission in top_submissions:
                twitter.update_status("https://reddit.com" + submission.permalink)
                time.sleep(INTERVAL)
        except tweepy.TweepError:
            pass
        
FoodBot()