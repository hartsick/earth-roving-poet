import os

twitter_cred = [
    os.environ.get('MASTER_BOT_CONSUMER_KEY'),
    os.environ.get('MASTER_BOT_CONSUMER_SECRET'),
    os.environ.get('EARTHROVER_ACCESS_TOKEN'),
    os.environ.get('EARTHROVER_ACCESS_TOKEN_SECRET')
]

BOT_ID = 3196974433

DEBUG = os.environ.get('TWEET_LOCAL', None)

# BOT-SPECIFIC CONFIG
