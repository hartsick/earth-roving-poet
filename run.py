from time import sleep
from twython import Twython
import config
from twitter.stream import UserStreamer

def do_the_thing():
    while True:
        try:
            stream = UserStreamer(*config.christa_cred)
            stream.user(**{'with': 'user'})
        except Exception as e:
            print(e)
            sleep(60)

if __name__ == "__main__":
    '''
        Because of Heroku's new limits for free dynos, the script will be auto-powered
        down for at least 6 hours per day. As such, I need to schedule the script
        to be run once per day, preferably at the start of my normal day (~7-8am PST)
        since it'll be listening for me tweeting. Since it's not a complicated schedule
        and I really don't care how accurate it is, I'm just using the free Heroku
        scheduler add-on. TMI maybe, but there you go.
    '''

    do_the_thing()
