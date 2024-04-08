import tweepy
import pandas as pd
from utils.config import *

cfg = Configs()
conf = cfg.get_data_config()

#print(conf)
consumer_key = conf['api_key']
consumer_secret = conf['api_key_secret']
access_token = conf['access_token']
access_token_secret = conf['access_token_secret']

auth = tweepy.OAuth1UserHandler(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret
    )

auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

search_query = "'annamalai ips''tamilnadu bjp'-filter:retweets AND -filter:replies AND -filter:links"
no_of_twits = 100

try:
    twits = api.search_tweets(q = search_query, count=no_of_twits, tweet_mode='extended')
    attributes_container = [[x.user.name, x.created_at, x.favorite_count, x.source, x.full_text] for x in twits]
    cols = ['user', 'date_created','num_of_likes','source_of_twit','twit']
    twits_df = pd.DataFrame(attributes_container,columns=cols)
except BaseException as ex:
    print(str(ex))
