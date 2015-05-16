import random
import time
from twython import Twython
import config

class Twy_REST(object):
    '''If run on remote, completes action via Twython and prints output. /
        Otherwise, if run locally, only prints to terminal.'''

    def __init__(self):
        self.twitter = Twython(*config.bot_cred)

    def follow_back(self, follow):
        if follow['source']['id'] is not config.BOT_ID:
            params = {'user_id': follow['source']['id'], 'screen_name': follow['source']['name']}

            if config.DEBUG:
                print "DEV: Friended {0} ({1})".format(follow['source']['name'], follow['source']['id'])
            else:
                try:
                    self.twitter.create_friendship(**params)
                except Exception as e:
                    print(e)

    def update_status(self, params):
        if config.DEBUG:
            print "DEV: updated status {0}".format(params)
        else:
            try:
                self.twitter.update_status(**params)
            except Exception as e:
                print(e)
