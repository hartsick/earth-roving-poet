from fixtures.tweets import sample_tweets
from twython import Twython
import config

class EarthRover(object):
    user_id = 2714673572
    username = "EarthRoverBot"

    def __init__(self, twitter):
        self.twitter = twitter

    def get_recent_statuses(self, number=100):
        '''
            By default, we're retrieving a lot of statuses because the count is
            requested before the replies and RTs are filtered out, meaning if
            someone (i.e. me) goes on a navigation bender, there's a small chance
            we won't get any usable tweets.
        '''
        if config.DEBUG:
            '''
            Probably want different tweet locally (i.e. still make request to server,
            just don't tweet) & debug (don't access server at all, use test fixtures
            instead) settings in future. For now, they're rolled into one.
            '''
            print "DEV: retrieving last {0} statuses".format(number)
            tweets = sample_tweets
        else:
            try:
                tweets = self.twitter.get_user_timeline(
                    user_id=self.user_id,
                    count=number,
                    exclude_replies=True,
                    include_rts=False
                )
            except Exception as e:
                print(e)
                return None

        return tweets

    @classmethod
    def get_media_url(cls, status):
        if status['entities']['media']:
            url = status['entities']['media'][0]['media_url']
            if config.DEBUG:
                print url
            return url

    @classmethod
    def get_status_url(cls, status):
        url = "http://twitter.com/{0}/status/{1}".format(cls.username, status['id_str'])
        if config.DEBUG:
            print url
        return url



if __name__ == '__main__':

    twitter = Twython(*config.bot_cred)
    bot = EarthRover(twitter)
    status = bot.get_recent_statuses(5)[-1]
    bot.get_media_url(status)
    bot.get_status_url(status)
