from time import sleep
from datetime import datetime
import config
from twitter.stream import UserStreamer

def do_the_thing():
    while True:
        # Only run stream between 7am - 1am PST
        if datetime.now().time().hour < 1 or datetime.now().time().hour > 7:
            try:
                stream = UserStreamer(*config.christa_cred)
                stream.user(**{'with': 'user'})
            except Exception as e:
                print(e)
                sleep(60)
        else:
            return

if __name__ == "__main__":
    '''
        Because of Heroku's new limits for free dynos, process should be scheduled
        to start ~6-7am PST every day, and will shut itself down at night.
    '''

    do_the_thing()
