from time import sleep
from twython import Twython
import config
import bot

def do_the_thing():
    twitter = Twython(*config.twitter_cred)
    text = "hello my future girlfriend"

    rover_status = EarthRover.get_most_recent_status(twitter)


    if config.DEBUG:
        print "LOCAL: Updated status with: '{0}'".format(text)
    else:
        try:
            twitter.update_status(status=text)
            print "REMOTE: Updated status with: '{0}'".format(text)
        except Exception as e:
            print(e)

if __name__ == "__main__":

    do_the_thing()
