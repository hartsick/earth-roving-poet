import random
import time
from twython import Twython
import config

class Twy_REST(object)
    '''If run on remote, completes action via Twython and prints output. /
        Otherwise, if run locally, only prints to terminal.'''

    def __init__(self):
        self.twitter = Twython(*config.bot_cred)

    def update_status(self, params):
        if config.DEBUG:
            print "DEV: updated status {0}".format(params)
        else:
            try:
                self.twitter.update_status(**params)
            except Exception as e:
                print(e)
