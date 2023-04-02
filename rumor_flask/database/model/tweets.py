"""
the "tweets" in the Mysql
"""

from database.database import db
from datetime import datetime
import pytz

class Tweets(db.Model):
    __tablename__ = 'tweets'
    keywords = db.Column(db.String(1023))
    tweet_text = db.Column(db.String(2047))
    tweet_id = db.Column(db.String(255), primary_key=True)
    user_name = db.Column(db.String(255))
    user_id = db.Column(db.String(255))
    user_followers_count = db.Column(db.String(255))
    user_friends_count = db.Column(db.String(255))
    images_url = db.Column(db.String(2047))
    create_time = db.Column(db.String(255))
    retweet_count = db.Column(db.String(255))
    likes_count = db.Column(db.String(255))

    @staticmethod
    def anything():
        pass

    def to_dict(self):
        date_format = "%a %b %d %H:%M:%S %z %Y"
        parsed_time = datetime.strptime(self.create_time, date_format)

        beijing = pytz.timezone('Asia/Shanghai')
        parsed_time = parsed_time.astimezone(beijing)

        new_date_format = "%Y-%m-%d %H:%M:%S"
        new_date_string = parsed_time.strftime(new_date_format)
        return {
            'keywords': self.keywords,
            'tweet_text': self.tweet_text,
            'tweet_id': self.tweet_id,
            'user_name': self.user_name,
            'user_id': self.user_id,
            'user_followers_count': self.user_followers_count,
            'user_friends_count': self.user_friends_count,
            'images_url': self.images_url,
            'create_time': new_date_string,
            'retweet_count': self.retweet_count,
            'likes_count': self.likes_count
        }
