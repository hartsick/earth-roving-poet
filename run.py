import logging
from time import sleep
from twython import Twython
from config.common import twitter_cred, tweet_locally

def do_the_thing():

    text = "hello my future girlfriend"

    if tweet_locally:
        print "LOCAL: Updated status with: '{0}'".format(text)
    else:
        try:
            Twython(*twitter_cred).update_status(status=text)
            print "REMOTE: Updated status with: '{0}'".format(text)
        except Exception as e:
            logging.exception(e)

if __name__ == "__main__":

    do_the_thing()
