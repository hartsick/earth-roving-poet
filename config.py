import os

bot_cred = [
    os.environ.get('MASTER_BOT_CONSUMER_KEY'),
    os.environ.get('MASTER_BOT_CONSUMER_SECRET'),
    os.environ.get('EARTHROVER_ACCESS_TOKEN'),
    os.environ.get('EARTHROVER_ACCESS_TOKEN_SECRET')
]

christa_cred = [
    os.environ.get('MASTER_BOT_CONSUMER_KEY'),
    os.environ.get('MASTER_BOT_CONSUMER_SECRET'),
    os.environ.get('CHRISTA_ACCESS_TOKEN'),
    os.environ.get('CHRISTA_ACCESS_TOKEN_SECRET')
]

BOT_ID = 3196974433
CHRISTA_ID = 24398192
ROVER_ID = 2714673572

DEBUG = os.environ.get('TWEET_LOCAL', None)
