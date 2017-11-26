import tweepy
import time


def get_mail():
    while True:
        try:
            user = api.verify_credentials('nataraja_siva',include_email=True)
            # https://api.twitter.com/1.1/account/verify_credentials.json?include_email=true
            d = {'name': user.name,
                 'screen_name': user.screen_name,
                 'id': user.id,
                 'friends_count': user.friends_count,
                 'followers_count': user.followers_count,
                 'followers_ids': user.followers_ids(),
                 }
            return user
        except tweepy.TweepError as e:
            if ('88' in e.reason):
                print('Wait: 15 min\n')
                time.sleep(60 * 15)
            else:
                print('Name not exist! You try with another name\n')
                exit()






# enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''  # keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''  # keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''  # keep the quotes, replace this with your access token
ACCESS_SECRET = ''  # keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify=True)

user_info=get_mail()
print(user_info)
