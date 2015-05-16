from time import sleep
from twython import Twython
import config
from image_to_text import ImageToText
from earth_rover import EarthRover

def do_the_thing():
    twitter = Twython(*config.twitter_cred)

    rover_status = EarthRover(twitter).get_recent_statuses()[-1]
    img_url = EarthRover.get_media_url(rover_status)

    text = ImageToText(img_url).top_caption()
    text += " " + EarthRover.get_status_url(rover_status)

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
