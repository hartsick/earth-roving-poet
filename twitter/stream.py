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
                print "Received earthrover fave!"
                self.on_fave(data)
        else:
            print "other"

    def on_error(self, status_code, data):
        print "{0} error: {1} | {2}".format(self.__class__.__name__, status_code, data)


    def is_earthrover_fave(self, status):
        return status['event'] == 'favorite' and status['source']['id'] == config.CHRISTA_ID and status['target']['id'] == config.ROVER_ID

    def on_fave(self, status):
        target = status['target_object']

        img_url = EarthRover.get_media_url(target)
        resp = ImageToText(img_url)
        text = resp.last_caption()
        text += " " + EarthRover.get_status_url(target)

        resp.log_interesting_data()

        if config.DEBUG:
            print "LOCAL: Updated status with: '{0}'".format(text)
        else:
            try:
                Twy_REST().update_status({'status': text})
                print "REMOTE: Updated status with: '{0}'".format(text)
            except Exception as e:
                print(e)
