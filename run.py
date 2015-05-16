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

    do_the_thing()
