from fixtures.sample_tweets import sample_tweets
from twython import Twython
import config

class EarthRover(object):
    def __init__(self, twitter):
        self.twitter = twitter
        self.user_id = 2714673572

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


if __name__ == '__main__':

    # EarthRover(twitter).get_recent_statuses()
    twitter = Twython(*config.twitter_cred)
    print(EarthRover(twitter).get_recent_statuses(5))
