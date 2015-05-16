from twython import TwythonStreamer
import config
from rest import Twy_REST
from bot.earth_rover import EarthRover
from bot.image_to_text import ImageToText

class UserStreamer(TwythonStreamer):
    '''
        Defines event handlers for the User stream
    '''
    def on_success(self, data):

        if data.get('event'):
            if self.is_earthrover_fave(data):
                print "is earthrover fave!"
                print data
                self.on_fave(data)
            elif self.is_follow(data):
                print "is follow!"
                print data
                self.on_follow(data)
        else:
            print "other"

    def on_error(self, status_code, data):
        print "{0} error: {1} | {2}".format(self.__class__.__name__, status_code, data)


    def is_earthrover_fave(self, status):
        return status['event'] == 'favorite' and status['source']['id'] == config.CHRISTA_ID

    def is_follow(self, data):
        return data['event'] == 'follow'

    def on_fave(self, status):
        target = status['target_object']

        img_url = EarthRover.get_media_url(target)
        text = ImageToText(img_url).top_caption()
        text += " " + EarthRover.get_status_url(target)

        if config.DEBUG:
            print "LOCAL: Updated status with: '{0}'".format(text)
        else:
            try:
                Twy_REST().update_status({'status': text})
                print "REMOTE: Updated status with: '{0}'".format(text)
            except Exception as e:
                print(e)

    def on_follow(self, follow):
        Twy_REST().follow_back(follow)
