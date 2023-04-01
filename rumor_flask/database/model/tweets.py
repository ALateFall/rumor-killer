"""
the "tweets" in the Mysql
"""

from app import db


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
