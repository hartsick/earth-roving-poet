import os

twitter_cred = [
    os.environ.get('MASTER_BOT_CONSUMER_KEY'),
    os.environ.get('MASTER_BOT_CONSUMER_SECRET'),
    os.environ.get('EARTHROVER_ACCESS_TOKEN'),
    os.environ.get('EARTHROVER_ACCESS_TOKEN_SECRET')
]

DEBUG = os.environ.get('TWEET_LOCAL', None)
